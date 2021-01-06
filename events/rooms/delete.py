from discord.channel import VoiceChannel
from discord.guild import Guild
from discord.member import Member, VoiceState

from aisha import Aisha
import db.api

aisha = Aisha()


async def delete_temporary_channel(before: VoiceState) -> bool:
    channel: VoiceChannel = before.channel
    if not channel:
        return False
    if channel.members:
        return False
    if channel.id not in db.api.get_temporary_channels_ids():
        return False
    await delete_temporary_channel_in_discord_with_db_updates(channel)
    return True


async def delete_temporary_channel_in_discord_with_db_updates(
        channel: VoiceChannel):
    await channel.delete()
    await db.api.delete_temporary_channel(channel.id)
