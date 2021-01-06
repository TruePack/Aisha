from discord.channel import VoiceChannel
from discord.member import Member, VoiceState

from aisha import Aisha
from events.rooms.create import create_temporary_channel
from events.rooms.delete import delete_temporary_channel

aisha = Aisha()


@aisha.listen()
async def on_voice_state_update(member: Member, before: VoiceState,
                                after: VoiceState):
    completed = await create_temporary_channel(member, after)
    if completed:
        return
    completed = await delete_temporary_channel(before)
    if completed:
        return


def init_events():
    pass
