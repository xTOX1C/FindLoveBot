from highrise import *
from highrise.models import *

async def fight(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    users = [content[0] for content in response.content]
    usernames = [user.username.lower() for user in users]
    parts = message[1:].split()
    args = parts[1:]
            
    if len(args) < 1:
        await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
        return
    elif args[0][0] != "@":
        await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
        return
    elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
        return
            
    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
    if not user_id:
        await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
        return
            
    try:
        await self.highrise.chat(f"\n🥷 @{user.username} And @{args[0][1:]} Fighting With Each Other 🤺")
        await self.highrise.send_emote("emote-swordfight", user.id)
        await self.highrise.send_emote("emote-swordfight", user_id)
    except Exception as e:
        print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

async def punk(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    users = [content[0] for content in response.content]
    usernames = [user.username.lower() for user in users]
    parts = message[1:].split()
    args = parts[1:]
            
    if len(args) < 1:
        await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
        return
    elif args[0][0] != "@":
        await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
        return
    elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
        return
            
    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
    if not user_id:
        await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
        return
            
    try:
        await self.highrise.send_emote("emote-punkguitar", user.id)
        await self.highrise.send_emote("emote-punkguitar", user_id)
    except Exception as e:
        print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

async def flirt(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    users = [content[0] for content in response.content]
    usernames = [user.username.lower() for user in users]
    parts = message[1:].split()
    args = parts[1:]
            
    if len(args) < 1:
        await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
        return
    elif args[0][0] != "@":
        await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
        return
    elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
        return
            
    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
    if not user_id:
        await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
        return
            
    try:
        await self.highrise.chat(f"\n 😏 @{user.username} And @{args[0][1:]} Flirting On Each Other 😏❤️")
        await self.highrise.send_emote("emote-lust", user.id)
        await self.highrise.send_emote("emote-lust", user_id)
    except Exception as e:
        print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

async def kiss(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    users = [content[0] for content in response.content]
    usernames = [user.username.lower() for user in users]
    parts = message[1:].split()
    args = parts[1:]
            
    if len(args) < 1:
        await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
        return
    elif args[0][0] != "@":
        await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
        return
    elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
        return
            
    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
    if not user_id:
        await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
        return
            
    try:
        await self.highrise.send_emote("emote-kiss", user.id)
        await self.highrise.send_emote("idle-loop-shy", user_id)
    except Exception as e:
        print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

async def hug(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    users = [content[0] for content in response.content]
    usernames = [user.username.lower() for user in users]
    parts = message[1:].split()
    args = parts[1:]
            
    if len(args) < 1:
        await self.highrise.send_whisper(user.id, f"Usage: !{parts[0]} <@username>")
        return
    elif args[0][0] != "@":
        await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
        return
    elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
        return
            
    user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
    if not user_id:
        await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
        return
            
    try:
        await self.highrise.send_emote("emote-hug", user.id)
        await self.highrise.send_emote("emote-hug", user_id)
    except Exception as e:
        print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")