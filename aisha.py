from discord.ext import commands

from consts import AISHA_PREFIX


class Aisha:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = commands.Bot(command_prefix=AISHA_PREFIX)
        return cls.__instance
