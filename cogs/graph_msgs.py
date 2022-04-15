from discord.ext import commands
import matplotlib.pyplot as plt
import discord
import io

class GraphMsgs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def graph_msgs(self, ctx, num=100):
        if num > 200:
            await ctx.send("Too many messages")
            return
        # get last 100 messages 
        msgs = await ctx.channel.history(limit=num).flatten()
        # get the message content
        msgs = [msg.content for msg in msgs]
        # parse through words and add to json
        words = {}
        for msg in msgs:
            for word in msg.split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        # clear words mentions less than 5 times
        for word in list(words.keys()):
            if words[word] < 2:
                del words[word]

        # sort the words by frequency
        dictionary = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
        # create the graph
        xAxis = [key for key, value in dictionary.items()]
        yAxis = [value for key, value in dictionary.items()]
        plt.grid(True)

        fig = plt.figure()
        plt.bar(xAxis,yAxis, color='maroon')
        plt.xlabel('Word')
        plt.ylabel('Frequency')
        plt.title('Last {} Word Frequencies'.format(num))
        plt.xticks(rotation=90, fontsize=3)

        # send the graph in embed format
        data_stream = io.BytesIO()
        plt.savefig(data_stream, format="png", dpi=1000)
        data_stream.seek(0)
        chart = discord.File(data_stream,filename="graph.png")
        e = discord.Embed(title='Last {} Word Frequencies'.format(num), description='', color=0x00ff00)
        e.set_image(url="attachment://graph.png")
        await ctx.send(embed=e, file=chart)
        data_stream.flush()
        data_stream.close()
        plt.close()

def setup(bot):
    bot.add_cog(GraphMsgs(bot))