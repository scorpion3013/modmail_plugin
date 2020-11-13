from discord.ext import commands
import discord

class ReactionClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        msg = thread.genesis_message
        print(msg)
        print(thread)
        await msg.add_reaction("🔒")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if not payload.guild_id:
            return
        emote = payload.emoji.name if payload.emoji.id is None else str(payload.emoji.id)
        emoji = payload.emoji.name if payload.emoji.id is None else payload.emoji

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if member.bot:
            return
        print(emote)
        print(emoji)
def setup(bot):
    bot.add_cog(ReactionClose(bot))
