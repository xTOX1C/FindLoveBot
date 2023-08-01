from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *

from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *

async def wear(self: BaseBot, user: User, message: str):
    _mods = ["maddy_16_01", "ad_e.l", "idumbo", "sassika", "ekichirou", "ogtoxic", "silverchain07", "ayybubbls", "_eclipxe", "babyytwinkles"]
    
    if user.username.lower() in _mods:
        pass
    else:
        await self.highrise.send_whisper(user.id, "You do not have permission to use this command.")
        return
    
    parts = message.split(" ")
    
    if len(parts) < 2:
        await self.highrise.chat("You need to specify the item name.")
        return
    
    item_name = ""
    for part in parts[1:]:
        item_name += part + " "
    item_name = item_name[:-1]
    
    item = (await self.webapi.get_items(item_name=item_name)).items
    
    if item == []:
        await self.highrise.chat(f"Item '{item_name}' not found.")
        return
    elif len(item) > 1:
        await self.highrise.chat(f"Multiple items found for '{item_name}', using the first item in the list {item[0].item_name}.")
    
    item = item[0]
    item_id = item.item_id
    category = item.category
    
    verification = False
    
    inventory = (await self.highrise.get_inventory()).items
    
    for inventory_item in inventory:
        if inventory_item.id == item_id:
            verification = True
            break
    
    if verification == False:
        if item.rarity == Rarity.NONE:
            pass
        elif item.is_purchasable == False:
            await self.highrise.chat(f"Item '{item_name}' can't be purchased.")
            return
        else:
            try:
                response = await self.highrise.buy_item(item_id)
                if response != "success":
                    await self.highrise.chat(f"Item '{item_name}' can't be purchased.")
                    return
                else:
                    await self.highrise.chat(f"Item '{item_name}' purchased.")
            except Exception as e:
                print(e)
                await self.highrise.chat(f"Exception: {e}'.")
                return
    
    new_item = Item(type="clothing", amount=1, id=item_id, account_bound=False, active_palette=0)
    
    outfit = (await self.highrise.get_my_outfit()).outfit
    
    for outfit_item in outfit:
        item_category = outfit_item.id.split("-")[0]
        if item_category == category:
            outfit.remove(outfit_item)
            break
    
    outfit.append(new_item)
    await self.highrise.set_outfit(outfit)
