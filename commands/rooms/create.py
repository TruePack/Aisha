from typing import List, Generator

from discord.ext.commands.context import Context
from discord.message import Message
from discord.member import Member
from discord.abc import GuildChannel
from discord.channel import CategoryChannel, VoiceChannel
from discord.guild import Guild
import db.api
from aisha import Aisha

aisha = Aisha()


@aisha.command(name="create_creator_room,")
async def create_creator_room(ctx: Context):
    message: Message = ctx.message
    guild: Guild = ctx.guild
    author: Member = ctx.author
    if not author.guild_permissions.administrator():
        await ctx.send("Bad permission, you must be administrator")
        return
    # command looks like
    # Aisha, create_creator_room, category=Голосовые каналы, channel_name=Фарм
    try:
        args: List[str] = message.clean_content.split(", ")
        category_name = args[2].split("=")[1]
        channel_name = args[3].split("=")[1]
    except Exception:
        await ctx.send(
            "Something wrong with command format, make sure commands looks "
            "like: \n"
            "```"
            "Aisha, create_creator_room, category=Voice Channels, "
            "channel_name=Farm"
            "```")
        return
    categories = aisha.get_all_channels()
    category: CategoryChannel = await get_or_create_category_for_creator_room(
        guild, categories, category_name)
    channel: VoiceChannel = await create_channel_in_discord_with_db_updates(
        guild, category, channel_name)
    await ctx.send(f"Channel created: {category} -> {channel.name}")


def filter_categories(all_channels: Generator[GuildChannel, None, None]
                      ) -> List[CategoryChannel]:
    categories = []
    for channel in all_channels:
        if isinstance(channel, CategoryChannel):
            categories.append(channel)
    return categories


async def get_or_create_category_for_creator_room(
        guild: Guild, categories: List[CategoryChannel],
        category_name: str) -> CategoryChannel:
    for category in categories:
        if category.name == category_name:
            return category
    else:
        category = await guild.create_category(category_name)
        return category


async def create_channel_in_discord_with_db_updates(guild: Guild,
                                                    category: CategoryChannel,
                                                    channel_name: str,
                                                    ) -> VoiceChannel:
    creator_channel: VoiceChannel = await guild.create_voice_channel(
        channel_name, category=category)
    await db.api.create_creator_channel(creator_channel.id)
    return creator_channel
