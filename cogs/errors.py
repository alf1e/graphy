from discord.ext import commands
import discord
import datetime

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction("❓")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(f"Chill, you're on cooldown for {error.retry_after:.2f}s")
        elif isinstance(error, commands.CheckFailure):
            await ctx.message.add_reaction("❓")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("🔐 I cant do that")
        elif isinstance(error, AttributeError):
            await ctx.reply("You need to make an account with dg!start")
        else:
            embed = discord.Embed(title="An error has occurred", description=f"```{error}```")
            embed.set_footer(text=f"Caused by {ctx.author.name}. Error has been reported", icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
            #embed = discord.Embed(title=f"An error has in `{ctx.guild.name}`@`{ctx.guild.id}` at `{datetime.datetime.now()}`", description=f"```{error}```")
            #embed.set_footer(text=f"Caused by {ctx.author.name} ", icon_url=ctx.author.avatar_url)
            #await self.bot.get_channel(958816042828849212).send(embed=embed)

def setup(bot):
    bot.add_cog(error(bot))