import discord
from discord.ext import commands


class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dispatch', aliases=['sos', 'notruf', '911', '110'])
    async def dispatch(self, ctx):
        await ctx.send(f'**<@&1099355811798593647>, <@&1099355808539623494>**')
        embed = discord.Embed(
            title='**Jemand hat den Notruf getätigt**',
            description=f'Alle verfügbaren Einheiten, es wurde ein Dispatch angefordert! bitte zu den Kooardinaten von {ctx.author.mention} anfahren!',
            color=discord.Color.blue()
        )
        embed.add_field(name='', value='', inline=False)
        embed.add_field(name='__**Überlebenszeit:**__', value='Die Medics haben 10 Minuten Zeit um bewusstlose Personen zu retten!')
        embed.set_footer(text=f'Dieser Notruf wird in 30 Minuten verfallen!')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1097441170273087528/1142443473048440832/Ems36.webp')
        embed.set_image(url='https://cdn.discordapp.com/attachments/1097441170273087528/1107688130364047412/LSMD_Eingangsbereich.png')

        await ctx.send(embed=embed)



async def setup(bot, add_cog=None):
    await bot.add_cog(Greet(bot))
