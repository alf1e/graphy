from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Displays the bots ping"""
        await ctx.message.add_reaction("🏓")
        bot_ping = round(self.bot.latency * 1000)
        if bot_ping < 130:
            color = 0x44FF44
        elif 130 < bot_ping < 180:
            color = 0xFF8C00
        else:
            color = 0xFF2200
        embed = discord.Embed(
            title="Pong! :ping_pong:",
            description=f"The ping is **{bot_ping}ms!**",
            color=color,
        )
        await ctx.reply(embed=embed)
    
def setup(bot):
    bot.add_cog(Admin(bot))