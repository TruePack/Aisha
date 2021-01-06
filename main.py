import os

import commands
import events
from aisha import Aisha
from consts import AISHA_TOKEN


def init():
    events.init_events()
    commands.init_commands()


def main():
    token = os.getenv(AISHA_TOKEN)
    init()
    aisha = Aisha()
    aisha.run(token)


if __name__ == '__main__':
    main()

