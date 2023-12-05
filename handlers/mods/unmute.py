from highrise import *
from highrise.models import *
        
async def unmute(self, user: User, message: str) -> None:
    _bid = "6448f9d57e36fb8bb4e65cb6"
    _uri = "644c84fc64d782bbf8721bc5"
    _id = f"1_on_1:{_bid}:{_uri}"
    _idx = f"1_on_1:{_uri}:{_bid}"
    parts = message.split()
    if len(parts) != 2:
        await self.highrise.send_whisper(user.id, "invalid mute format. \n!unmute @username")
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
        await self.highrise.moderate_room(user_id, "mute", 1)
        try:
            await self.highrise.send_message(_id, f"Action : unmute\nunmuted by : @{user.username}\nunmuted user : @{username}", "text")
        except:
            await self.highrise.send_message(_idx, f"Action : unmute\nunmuted by : @{user.username}\nunmuted user : @{username}", "text")
    except Exception as e:
        await self.highrise.send_whisper(user.id, f"{e}")
        return
    await self.highrise.send_whisper(user.id, f"{username} muted for {parts[2]} seconds.")
