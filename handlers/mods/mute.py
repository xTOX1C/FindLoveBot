from highrise import *
from highrise.models import *

async def mute(self, user: User, message: str) -> None:
    _mods = ["maddy_16_01", "ad_e.l", "idumbo", "sassika", "ekichirou", "ogtoxic", "silverchain07", "ayybubbls", "_eclipxe", "babyytwinkles"]

    _bid = "6448f9d57e36fb8bb4e65cb6"
    _uri = "644c84fc64d782bbf8721bc5"
    _id = f"1_on_1:{_bid}:{_uri}"
    _idx = f"1_on_1:{_uri}:{_bid}"

    if user.username.lower() in _mods:
        pass
    else:
        await self.highrise.send_whisper(user.id, "You do not have permission to use this command.")
        return
    parts = message.split()
    if len(parts) != 3:
        await self.highrise.send_whisper(user.id, "invalid mute format. \n-mute @username 60")
        return
    if "@" not in parts[1]:
        username = parts[1]
    else:
        username = parts[1][1:]
    room_users = (await self.highrise.get_room_users()).content
    for room_user, pos in room_users:
        if room_user.username.lower() == username.lower():
            user_id = room_user.id
            break
    if "user_id" not in locals():
        await self.highrise.send_whisper(user.id, "User not found in room.")
        return
    try:
        await self.highrise.moderate_room(user_id, "mute", parts[2])
        try:
            await self.highrise.send_message(_id, f"Action : mute\muted by : @{user.username}\nmuted user : @{username}\nMute length : {parts[2]}", "text")
        except:
            await self.highrise.send_message(_idx, f"Action : mute\nmuted by : @{user.username}\nmuted user : @{username}\nMute length : {parts[2]}", "text")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"{e}")
        return
    await self.highrise.send_whisper(user.id, f"{username} muted for {parts[2]} seconds.")