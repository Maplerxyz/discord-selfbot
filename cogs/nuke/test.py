from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f"This is a test response for a cog!")

def setup(client):
    client.add_cog(test(client))