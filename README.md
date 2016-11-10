# DamianBot for Discord
Personal Discord bot using Discord.py API Wrapper

#Setting it up
## [Bot.py](./bot.py)
On line 55 You will need to replace 'TOKEN HERE' with your bot's token.

```python
if __name__ == '__main__':
    token = 'TOKEN HERE'
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
```

## [SeachOnline.py](./commands/searchonline.py)
On line 35 and 40 you must replace 'GOOGLEAPIAUTHKEY' with your google api auth key which you need to register with the google api.

```python
async def eat(self, ctx):
    gmaps = googlemaps.Client(key='GOOGLEAPIAUTHKEY')
    loc = ctx.message.content[len('!eat'):].strip()
    geocode_result = gmaps.geocode(str(loc))

    def GoogPlac(lat,lng,radius,types):
      AUTH_KEY = 'GOOGLEAPIAUTHKEY'
```

## YES! I could have made this easier to 'config'
I actually did not plan on releasing this on Github, but decided, why not. So here it is and I will maintain updates on it with new features.
The math command I am still working on perfecting the parsed data SENT and RECIEVED, since if there is a fraction it will be /FRAC{#}{#}
So for now with the math function, keep it simple stupid. Be careful spamming the !eat function, google will ban you.
