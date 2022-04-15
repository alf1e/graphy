from discord.ext import commands
import matplotlib.pyplot as plt
import discord
import io

class GraphMostMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def graph_most_messages(self, ctx):
        # get all members in the servers messages
        members = ctx.guild.fetch_members()
        members_new = []
        # remove bots from memebers
        async for member in members:
            if not member.bot:
                members_new.append(member)
        members = members_new
        # get the amount of messages from eacxh user
        messages = {}
        for member in members:
            messages[member.name] = len(await member.history().flatten())

        # remove users with under 5000 messages
        messages_new = {}
        for key, value in messages.items():
            if value > 5000:
                messages_new[key] = value
        messages = messages_new
        print(messages)
        # build graph
        xAxis = [key for key, value in messages.items()]
        yAxis = [value for key, value in messages.items()]
        plt.grid(True)
        plt.figure()
        plt.bar(xAxis,yAxis, color='maroon')
        plt.xlabel('User')
        plt.ylabel('Number of Messages')
        plt.title('Number of Messages per User')
        plt.xticks(rotation=90, fontsize=8)

        data_stream = io.BytesIO()
        plt.savefig(data_stream, format="png")
        data_stream.seek(0)
        chart = discord.File(data_stream,filename="graph.png")
        e = discord.Embed(title='Number of messages per user', description='', color=0x00ff00)
        e.set_image(url="attachment://graph.png")
        await ctx.send(embed=e, file=chart)
        data_stream.flush()
        data_stream.close()
        plt.close()

def setup(bot):
    bot.add_cog(GraphMostMessages(bot))