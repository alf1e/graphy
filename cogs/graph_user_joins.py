from discord.ext import commands
import matplotlib.pyplot as plt
import io
import discord

class GraphUserJoins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def graph_user_joins(self, ctx):
        # get all members in the server
        members = ctx.guild.fetch_members()
        members_new = []
        # remove bots from memebers
        async for member in members:
            if not member.bot:
                members_new.append(member)
        members = members_new
            
        month = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
        month_for = {}
        month_num = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        for member in members:
            month[member.joined_at.month] += 1
    
        for key, value in month.items():
            month_for[month_num[key]] = value
        month = month_for

        # create the graph
        xAxis = [key for key, value in month.items()]
        yAxis = [value for key, value in month.items()]
        plt.grid(True)
        plt.figure()
        plt.bar(xAxis,yAxis, color='maroon')
        plt.xlabel('Month')
        plt.ylabel('Number of Members')
        plt.title('Number of Member joins per Month')
        plt.xticks(rotation=90, fontsize=8)

        data_stream = io.BytesIO()
        plt.savefig(data_stream, format="png")
        data_stream.seek(0)
        chart = discord.File(data_stream,filename="graph.png")
        e = discord.Embed(title='Number of member joins per month', description='', color=0x00ff00)
        e.set_image(url="attachment://graph.png")
        await ctx.send(embed=e, file=chart)
        data_stream.flush()
        data_stream.close()
        plt.close()

def setup(bot):
    bot.add_cog(GraphUserJoins(bot))