from discord.ext import commands
import discord
from random import randint
import asyncio

class BasicCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='crashserver', pass_context=True, help='The greatest thing in the world is destruction!')
    async def crashserver(self, ctx):
        await self.bot.say('{0.mention} just tried to crash the server!'.format(ctx.message.author))

    @commands.command(name='creator', help='How can I have a creator if I am not a bot?')
    async def creator(self):
        await self.bot.type()
        await asyncio.sleep(5)
        await self.bot.say('I am not a bot...?')

    @commands.command(name='streams', pass_context=True, help='Check who is streaming.')
    async def streams(self, ctx):
        streams = []
        streamers = '{} is streaming {} at {}'
        for member in ctx.message.server.members:
            if member.game != None:
                if member.game.type != 0:
                    streams.append(streamers.format(member, member.game, member.game.url))
        if not streams:
            await self.bot.say('Looks like nobody is streaming right now...')
        else:
            streams = '\n'.join(streams)
            await self.bot.say(streams)

    @commands.command(name='stdtest', help='We know you\'ve been curious, let\'s find out!')
    async def stdtest(self):
        std = [
        'Clean 	 • You are clean!',
        'Chancroid 	 • treatable STD, bacterial infection that causes painful sores.',
        'Chlamydia 	 • treatable STD, bacterial infection of the prostate, urethra & female pelvis.',
        'Crabs (Lice) 	 • treatable STD, parasites or bugs that live on the pubic hair in the genital area.',
        'Gonorrhea 	 • treatable STD, bacterial infection of the penis, vagina or anus, aka “the clap”',
        'Hepatitis 	 • five types; A & E are self-limiting; B, C, & D are cureless; B is preventable with a vaccine',
        'Herpes 	 • treatable but often recurrent STD, viral infection causing blisters (anus, vagina, penis).',
        'HIV / AIDS 	 • cureless STD, viral infection of the immune system (no cure fo this STD)',
        'HPV / Warts 	 • cureless STD, viral infection of the skin in the genital area & female’s cervix.',
        'Scabies 	 • treatable STD, mite parasites that burrows under the skin and lays eggs',
        'Syphilis 	 • treatable STD, bacterial infection affecting genitals, heart, & nerves.',
        'Trichomoniasis 	 • treatable STD, protozoan parasite infection of male urethra & female pelvis.',
        'Yeast Infection 	 • treatable fungal infection of the vagina',
        'Vaginosis 	 • treatable vaginal infection causing itch, burning, discharge & an odd odor',
        'Yeast in Men 	 • treatable fungal infection of the tip of the penis, called balanitis'
        ]
        await self.bot.say(std[randint(0,14)])


    """@bot.event
    async def on_message_edit(before, after):
        tmp = before.content
        if tmp.startswith("http"):
            return
        else:
            fmt = 'Uh oh {} changed a message from: \'{}\' | to:\'{}\''
            channel = discord.Object(id='242516917712060416')
            await bot.send_message(channel, fmt.format(before.author, before.content, after.content))"""

def setup(bot):
    bot.add_cog(BasicCommands(bot))
