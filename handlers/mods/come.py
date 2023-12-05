# come.py
from highrise import*
from highrise.models import* # Replace 'some_module' with the actual module where Position is defined

async def come(self, user: User, message: str) -> None:
    response = await self.highrise.get_room_users()
    your_pos = None
    for content in response.content:
        if content[0].id == user.id:
            if isinstance(content[1], Position):
                your_pos = content[1]
                break
    if not your_pos:
        await self.highrise.send_whisper(user.id, f"Location Error")
        return
    await self.highrise.send_whisper(user.id, f"On my way, @{user.username}")
    await self.highrise.walk_to(your_pos)
