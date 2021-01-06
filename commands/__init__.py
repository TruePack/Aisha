import os
from typing import Optional, List

from discord.guild import Guild
from aisha import Aisha
from commands import test
from commands import rooms
from discord.channel import TextChannel, VoiceChannel
from discord.abc import GuildChannel
from consts import GUILD_ID, AISHA_LOGS_CHANNEL_NAME

aisha = Aisha()


@aisha.event
async def on_ready():
    channel = get_aisha_logs_channel()
    if not channel:
        return
    await channel.send("Aisha connected, everything ok")


def get_aisha_logs_channel() -> TextChannel:
    guild_id = int(os.getenv(GUILD_ID))
    guild: Optional[Guild] = aisha.get_guild(guild_id)
    channels: List[Optional[VoiceChannel, TextChannel]] = guild.channels
    for channel in channels:
        if is_text_aisha_logs_channel(channel):
            return channel


def is_text_aisha_logs_channel(channel: GuildChannel) -> bool:
    if isinstance(channel, TextChannel):
        return channel.name == AISHA_LOGS_CHANNEL_NAME


@aisha.event
async def on_disconnect():
    channel = get_aisha_logs_channel()
    if not channel:
        return
    await channel.send("Aisha disconnected, something wrong")


def init_commands():
    pass
