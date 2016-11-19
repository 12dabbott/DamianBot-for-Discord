from discord.ext import commands
import asyncio

class Poll:
    def __init__(self, bot):
        self.bot = bot
        self.yesir = 0
        self.noir = 0
        self.pollstarted = False
        self.tmp = None
        self.pollir = ''

    @commands.command(name='poll', pass_context=True, help='Start a poll!')
    async def poll(self, ctx):
        if self.pollstarted:
            return
        self.pollstarted=True
        self.pollir = ctx.message.content[len('!poll'):].strip()
        self.tmp = await self.bot.say('2 minute poll: !yes : {} | !no : {} | \"{}\"'.format(self.yesir, self.noir, self.pollir))

        await asyncio.sleep(120)

        await self.bot.delete_message(self.tmp)
        await self.bot.say('Final results: !yes : {} | !no : {} | \"{}\"'.format(self.yesir, self.noir, self.pollir))
        self.yesir = 0
        self.noir = 0
        self.pollstarted = False
        self.tmp = None


    @commands.command(name='yes', help='Say yes to a poll!')
    async def yes(self):
        if not self.pollstarted:
            return
        self.yesir+=1

        await self.bot.edit_message(self.tmp, '2 minute poll: !yes : {} | !no : {} | \"{}\"'.format(self.yesir, self.noir, self.pollir))

    @commands.command(name='no', help='Say no to a poll!')
    async def no(self):
        if not self.pollstarted:
            return
        self.noir+=1

        await self.bot.edit_message(self.tmp, '2 minute poll: !yes : {} | !no : {} | \"{}\"'.format(self.yesir, self.noir, self.pollir))



def setup(bot):
    bot.add_cog(Poll(bot))
