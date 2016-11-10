from discord.ext import commands
import requests
import googlemaps
import json
from google import search
from random import randint
from bs4 import BeautifulSoup

class SearchOnline:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='steam', pass_context=True, help='Search information on a steam account, use the account\'s userid.')
    async def steam(self, ctx):
        player = ctx.message.content[len('!steam'):].strip()
        if player == "":
            await self.bot.say('Please specify a userid!')
            return
        else:
            payload = {'player': player, 'currency': 'us'}
            r = requests.get('https://steamdb.info/calculator/', params=payload)
            soup= BeautifulSoup(r.text, "lxml")
            desc= soup.find(attrs={'property':'Description'})
            if desc == None:
                desc= soup.find(attrs={'property':'description'})
            if desc['content'] == 'This page will calculate the approximate value of your Steam account by looking up your games on your Steam community profile, using the current prices for each game on the Steam store.':
                await self.bot.say("I couldn't find that steam user! Try their steamid!")
            else:
                tmp = desc['content'] + '\n' + 'https://steamcommunity.com/id/' + player
                await self.bot.say(tmp)

    @commands.command(name='eat', pass_context=True, help='Find a random place near you to eat at, just give a location.')
    async def eat(self, ctx):
        gmaps = googlemaps.Client(key='GOOGLEAPIAUTHKEY')
        loc = ctx.message.content[len('!eat'):].strip()
        geocode_result = gmaps.geocode(str(loc))

        def GoogPlac(lat,lng,radius,types):
          AUTH_KEY = 'GOOGLEAPIAUTHKEY'
          LOCATION = str(lat) + "," + str(lng)
          RADIUS = radius
          TYPES = types
          MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
                   '?location=%s'
                   '&radius=%s'
                   '&types=%s'
                   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
          r = requests.get(MyUrl)
          jsonData = json.loads(r.text)
          return jsonData

        def IterJson(place):
            x = randint(0,len(place['results']))
            xd = place['results'][x]
            if 'rating' in xd.keys():
                placex = 'You should try out: {} over on {} has a rating of {} out of 5!'.format(xd['name'], xd['vicinity'], xd['rating'])
            else:
                placex = 'You should try out: {} over on {}'.format(xd['name'], xd['vicinity'])
            return placex

        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        place = GoogPlac(lat, lng, 10000, 'restaurant')
        placex = IterJson(place)
        await self.bot.say(str(placex))

    @commands.command(name='math', pass_context=True, help='Solve any math problem. Still being worked on, keep your problems simple.')
    async def math(self, ctx):
        equation = ctx.message.content[len('!math'):].strip()
        equation.replace('=', '%3D')
        payload = {'userId': 'fe', 'query': equation, 'connected': '', 'language': 'en'}
        r = requests.get('https://www.symbolab.com/steps?', params=payload)
        jsonData = json.loads(r.text)
        answer = jsonData['solutions'][0]['entire_result']
        await self.bot.say(str(answer))

def setup(bot):
    bot.add_cog(SearchOnline(bot))
