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
    'commands.searchonline',
    'commands.poll'
]

callisays = ['bye', 'adios', 'cya']

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
    if 'kys' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, '(Keep yourself safe)')
    elif 'kms' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, 'If you need to talk, please call the Suicide Prevention Hotline at 1-800-273-TALK (8255) any time')
    elif any(x in message.content.lower() for x in callisays) and message.author.id == '236295255530536960':
        await bot.send_message(message.channel, 'What she means is: \"I prefer not to engage in this conversation\"')
    elif message.content.startswith('!callisays') and message.author != bot.user:
        global callisays
        calliword = message.content[len('!callisays'):].strip()
        if calliword == '' or calliword == ' ':
            await bot.send_message(message.channel, 'Current Calliwords: {}'.format(callisays))
            return
        calliword = calliword.lower()
        callisays.append(str(calliword))
        await bot.send_message(message.channel, 'Added {} to the list of words Calli uses when avoiding a conversation!'.format(str(calliword)))
    elif '!clearcalli' in message.content and message.author != bot.user:
        global callisays
        callisays = ['bye', 'adios', 'cya']
        await bot.send_message(message.channel, 'Okay! Reset Calli\'s words to {}'.format(callisays))
    elif 'burn' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.send_message(message.channel, 'https://en.wikipedia.org/wiki/List_of_burn_centers_in_the_United_States')
    elif 'retard' in message.content.lower() and message.author != bot.user and not message.content.startswith('!'):
        await bot.delete_message(message)



if __name__ == '__main__':
    token = 'TOKEN_HERE'
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(token)
