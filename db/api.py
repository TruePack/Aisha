from typing import List, Set

from memoize.wrapper import memoize


@memoize()
async def get_creator_channels_ids() -> Set[int]:
    pass


async def get_temporary_channels_ids() -> List[int]:
    pass


async def create_creator_channel(channel_id: int):
    pass


async def create_temporary_channel(channel_id: int):
    pass


async def delete_temporary_channel(channel_id: int):
    pass