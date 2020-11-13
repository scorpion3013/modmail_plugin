from discord.ext import commands
import discord

class ReactionClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels = {}
    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        msg = thread.genesis_message
        print(msg)
        print(thread)
        print(thread.channel.id)
        self.channels[thread.channel.id] = thread
        await msg.add_reaction("🔒")

    @commands.Cog.listener()
    async def on_thread_close(self, thread, closer, silent, delete_channel, message, scheduled):
        print(thread)
        print(closer)
        print(message)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if not payload.guild_id:
            return
        channel_id = payload.channel_id
        if not self.channels.keys().__contains__(channel_id):
            print("Not supported channel")
            return
        emote = payload.emoji.name if payload.emoji.id is None else str(payload.emoji.id)

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if member.bot:
            return

        if emote == "🔒":
            await self.channels.get(channel_id).close(closer=member, after=10)



def setup(bot):
    bot.add_cog(ReactionClose(bot))
