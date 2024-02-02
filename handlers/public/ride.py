from highrise import*
from highrise.models import*
from highrise.webapi import*
from highrise.models_webapi import*
import random
import asyncio

async def ride(self, user: User, message: str):
    # Assuming response is defined somewhere in your code
    response = await self.highrise.get_room_users()
    for content in response.content:
        if content[0].id == user.id:
            if isinstance(content[1], Position):
                your_pos = content[1]
                break

    for _ in range(5):
        # Assuming Position has appropriate constructor parameters
        await self.highrise.teleport(user.id, Position(random.randint(1, 18), random.randint(1, 30), random.randint(1, 30), "FrontLeft"))
        await asyncio.sleep(0.5)
        
    await self.highrise.teleport(user.id, your_pos)
