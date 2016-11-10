from discord.ext import commands
import discord
import sys


description = """
Written by Damian for our personal Discord!
"""

initial_extensions = [
    'commands.basic',
    'commands.ascii',
    'commands.chatbots',
    'commands.logcommands',
    'commands.searchonline'
]

help_attrs = dict(hidden=True)

prefix = ['!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None, help_attrs=help_attrs)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.send_message(server, fmt.format(member, server))

@bot.event
async def on_error(event, *args, **kwargs):
    err = sys.exc_info()
    fmt = 'I ran into an error! Send this to my owner: {}'
    channel = discord.Object(id='242516917712060416')
    await bot.send_message(channel, fmt.format(err))

@bot.listen()
async def on_message(message):
    if 'game' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, 'You lost it')
    elif 'wednesday' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, 'It\'s Tuesday you fucking retard')
    elif 'kys' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, '(Keep yourself safe)')


if __name__ == '__main__':
    token = 'TOKEN HERE'
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(token)
