from highrise import *
from highrise.models import *
import random

async def reaction(self, user: User, message: str) -> None:
    parts = message.split()
    args = parts[1:]
    _bid = "6448f9d57e36fb8bb4e65cb6"
    reactions = ["clap", "heart", "thumbs", "wave", "wink"]
    Rreaction = random.choice(reactions)
    roomUsers = (await self.highrise.get_room_users()).content
    if len(args) > 0 and args[0] in reactions:
        for roomUser, _ in roomUsers:
            if roomUser.id == _bid:
                pass
            else:
                await self.highrise.react(f"{args[0]}", roomUser.id)
    elif len(args) == 0:
        for roomUser, _ in roomUsers:
            if roomUser.id == _bid:
                pass
            else:
                await self.highrise.react(Rreaction, roomUser.id)