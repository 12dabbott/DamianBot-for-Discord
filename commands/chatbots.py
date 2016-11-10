from discord.ext import commands
from cleverbot import Cleverbot
from bs4 import BeautifulSoup
import json
import requests
import praw
from google import search

cb = Cleverbot()

class ChatBots:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chat', pass_context=True, help='Chat with me!')
    async def chat(self, ctx):
        question = ctx.message.content[len('!chat'):].strip()
        answer = cb.ask(question)
        await self.bot.say(answer)

    @commands.command(name='ask', pass_context=True, help='Ask me anything!')
    async def ask(self, ctx):
        question = ctx.message.content[len('!ask'):].strip()
        payload = {'q': question}
        r = requests.get('http://www.quickanswers.io/ask/', params=payload)
        soup = BeautifulSoup(r.text, 'lxml')
        soup2 = soup.text.replace('\t','').replace('\n\n','').replace('Click to validate this answer.','\n')
        answer = str(soup2)
        if answer == 'Sorry, I don\'t know.':
            for url in search(str(question), num=1, start=0, stop=1):
                answer = str(url)
        await self.bot.say(answer)

    @commands.command(name='reddit', pass_context=True, help='Find the top post and comment from any subreddit. Default is day, optional is all/year/month/week/hour')
    async def reddit(self, ctx):
        word = ctx.message.content[len('!reddit'):].strip()
        r = praw.Reddit('test')
        word = word.split()
        s = r.get_subreddit(word[0])
        if len(word) == 1 or word[1] == 'day':
            for sub in s.get_top_from_day(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
                word.append('day')
        elif word[1] == 'week':
            for sub in s.get_top_from_week(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
        elif word[1] == 'all':
            for sub in s.get_top_from_all(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
        elif word[1] == 'hour':
            for sub in s.get_top_from_hour(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
        elif word[1] == 'month':
            for sub in s.get_top_from_month(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
        elif word[1] == 'year':
            for sub in s.get_top_from_year(limit=1):
                sub = r.get_submission(submission_id=sub.id, comment_limit=1, comment_sort='top')
        else:
            await self.bot.say('Incorrect use... Syntax: !reddit [subreddit] [optional:hour,day,week,all]')
            return 0
        if sub.over_18 and 'nsfw' not in ctx.message.channel.name:
            await self.bot.say('Looks like you tried to post this in a SFW channel bud!')
            return 0
        flat_comments = praw.helpers.flatten_tree(sub.comments)
        if str(sub.url) != str(sub.permalink):
            x = 'Top post of {} from /{}/\n{}\n{}\n{}'.format(str(word[1]), str(word[0]), str(sub.title), str(sub.selftext), str(sub.url))
        else:
            x = 'Top post of {} from /{}/\n {}\n{}'.format(str(word[1]), str(word[0]), str(sub.title), str(sub.selftext))
        for comment in flat_comments:
            x += '\n' + 'The top comment is:\n' + str(comment.body)
            break
        if len(x) > 2000:
            x = x[:1999]
        await self.bot.say(x)

def setup(bot):
    bot.add_cog(ChatBots(bot))
