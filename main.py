import discord 
import discord.ext.commands as commands
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import io
# load dotenv
from dotenv import load_dotenv
load_dotenv()
admins = [692395545720913941, 677252870722027549]

bot = commands.Bot(command_prefix=["graph!", "g!", "Graph!"], intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.load_extension('jishaku')

@bot.command()
async def reload(ctx, to_reload=None):
  if ctx.author.id in admins:
    if not to_reload:
      embed = discord.Embed(title="Reloaded!")
      sys = await ctx.reply("Reloading")
      for file in os.listdir("cogs"):
        if file.endswith(".py"):
          try:
            bot.reload_extension(f'cogs.{file[:-3]}')
            embed.add_field(name="\u200b", value=f"🟩 Loaded `{file[:-3]}`", inline=False)
          except Exception as e:
            embed.add_field(name="\u200b", value=f"🟥 Failed to Load `{file[:-3]}` with error `{e}`", inline=False)
      await sys.edit(embed=embed)
    else:
      try:
        bot.reload_extension(f'cogs.{file[:-3]}')
        await ctx.reply(f"🟩 Reloaded `COGS.{to_reload}`")
      except Exception as e:
        await ctx.reply(f"🟥 Failed to reload `COGS.{to_reload}` with error `{e}`")

bot.run(os.getenv('TOKEN'))


    

