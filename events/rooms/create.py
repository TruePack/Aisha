from discord.channel import VoiceChannel, CategoryChannel
from discord.member import Member, VoiceState
from discord.guild import Guild

from aisha import Aisha
import db.api

aisha = Aisha()


@aisha.listen()
async def create_temporary_channel(member: Member, after: VoiceState) -> bool:
    channel: VoiceChannel = after.channel
    guild: Guild = channel.guild
    member_name: str = member.display_name

    if member.bot or not channel:
        return False

    if channel.id in await db.api.get_creator_channels_ids():
        category: CategoryChannel = channel.category
        temporary_channel: VoiceChannel = (
            await create_temporary_channel_in_discord_with_db_updates(
                guild, category, member_name))
        await member.move_to(temporary_channel)
        return True


async def create_temporary_channel_in_discord_with_db_updates(
        guild: Guild, category: CategoryChannel,
        member_name: str) -> VoiceChannel:
    """Create and update temporary channel in database"""
    channel: VoiceChannel = await guild.create_voice_channel(member_name,
                                                             category=category)
    await db.api.create_temporary_channel(channel.id)
    return channel
