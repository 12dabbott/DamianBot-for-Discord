from discord.ext import commands
import discord
from datetime import datetime, timedelta

class LogCommands():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='count', pass_context=True, help='Count how many times a word or phrase has been said in the last week.')
    async def count(self, ctx):
        word = ctx.message.content[len('!count'):].strip()
        counter = -1
        d = datetime.today() - timedelta(days=7)
        tmp = await self.bot.send_message(ctx.message.channel, 'Looking for {}...'.format(word))
        async for log in self.bot.logs_from(ctx.message.channel, limit=15000, before=None, after=d):
            if word.lower() in log.content.lower() and log.author != self.bot.user:
                counter += 1

        await self.bot.edit_message(tmp, '{} has been said, {} time(s) in the past week'.format(word, counter))

    @commands.command(name='quote', pass_context=True, help='Quote users who said specific things.')
    async def quote(self, ctx):
        quotethis = ctx.message.content[len('!quote'):].strip()
        lookfor = quotethis.split()
        quotes = []
        notfound = 'Hmm couldn\'t find that quote!'
        tmp = await self.bot.send_message(ctx.message.channel, 'Looking for a message with: {}'.format(quotethis))
        async for log in self.bot.logs_from(ctx.message.channel, limit=15000):
            if len(quotes) < 10:
                if all(word.lower() in log.content.lower() for word in lookfor) and log.author != self.bot.user and not log.content.startswith('!quote'):
                    found = '{} said: {}'
                    quotes.append(found.format(log.author, log.content))
            else:
                break
        if len(quotes) != 0:
            quotes.reverse()
            quotes = '\n'.join(quotes)
            await self.bot.edit_message(tmp, quotes)
        else:
            await self.bot.edit_message(tmp, notfound)

    @commands.command(name='purge', pass_context=True, hidden=True)
    async def purge(self, ctx):
        if ctx.message.author.id == '143880485968281602':
            def is_me(m):
                return m.author == self.bot.user
            def is_to_me(m):
                if m.content.startswith('!'):
                    return True

            deleted = await self.bot.purge_from(ctx.message.channel, limit=5000, check=is_me)
            deletedtoo = await self.bot.purge_from(ctx.message.channel, limit=5000, check=is_to_me)
            await self.bot.send_message(ctx.message.channel, 'Deleted {} message(s)'.format(len(deleted) + len(deletedtoo)))
        else:
            await self.bot.send_message(ctx.message.channel, 'You can\'t use this command!')

def setup(bot):
    bot.add_cog(LogCommands(bot))
