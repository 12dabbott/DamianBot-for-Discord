from discord.ext import commands
import re

class AsciiGenerator:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ascii', pass_context=True, help='Convert your text to ASCII. 20 Character limit.')
    async def ascii(self, ctx):
        sentence = ctx.message.content[len('!ascii'):].strip()
        if sentence == "":
            await self.bot.say('Please give me a message to ASCIIfy!')
            return
        elif len(sentence) > 20:
            await self.bot.say('Hold your horses! I have a 20 character limit !')
            return
        else:
            asc = [
            " #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###  #  ",
            "# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #  #  ",
            "### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##  #  ",
            "# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #           ",
            "# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #   #  "
            ]
            t = sentence.lower()
            t = [ord(x)-97 for x in t]
            ascsent = []
            for i in range(0,5):
                row = re.findall('....',asc[i])
                ans = []
                for x in t:
                    if x == -65:
                        ans.append("   ")
                    elif x == -64:
                        ans.append(row[27])
                    elif x < 26 or x > 0:
                        ans.append(row[x])
                    else:
                        ans.append(row[26])
                ans=''.join(ans)
                ascsent.append(ans)
            ascsent = '\n.'.join(ascsent)
            await self.bot.say("." + ascsent.replace(' ', '  '))

def setup(bot):
    bot.add_cog(AsciiGenerator(bot))
