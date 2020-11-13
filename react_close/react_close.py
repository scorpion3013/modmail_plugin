from discord.ext import commands


class ReactionClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        msg = thread.genesis_message
        print(msg)
        print(thread)


def setup(bot):
    bot.add_cog(ReactionClose(bot))
