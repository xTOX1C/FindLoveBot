from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
)
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
)
from asyncio import run as arun
import requests
import random
import asyncio
import os
import importlib
user_warnings = {}

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class Bot(BaseBot):

    async def advertisement(self):
        i = 1
        _ads = [
            "\n💰 Show support, tip the jar! 🎉\nHelp our room thrive with your support. #Gratitude ",
            "\n💻 Want Your Own Custom BOT? Contact @OGToxic for commissions. affordable, efficient, and reliable services.",
            "\n💕 Grateful for your presence! Thank you for being here, making this chat special.",
            "\n🤷 If you have any questions or need assistance, feel free to contact with mods. Your engagement means a lot!🙏",
        ]
        while True:
            for _ads_ in _ads:
                await self.highrise.chat(f"{_ads_} [{i}]")
                await asyncio.sleep(29)
                i += 1
    
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            await self.highrise.walk_to(Position(16.5, 1.25, 12.5, "FrontLeft"))
            await self.highrise.chat("Reconnected...")
            ad_task = asyncio.create_task(self.advertisement())
            await ad_task
        except Exception as e:
            print(f"error : {e}")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        text_to_emoji = {
        "wink": "😉",
        "wave": "👋",
        "thumbs": "👍",
        "heart": "❤️",
        "clap": "👏",
        }
        await self.highrise.chat(f"\n{user.username} {text_to_emoji[reaction]} {receiver.username}")

    async def on_user_join(self, user: User) -> None:
        try:
            print(f"{user.username} Joined Room.")
            wm = [
            'Welcome to the Find Ur Love ❤️, where hearts connect! Take a seat, let love find you. Don\'t hesitate to say hi and start a conversation. Embrace the magic of connection and let your journey begin!',
            'Step into the Find Ur Love ❤️, where souls intertwine! Find your special someone and break the ice with a friendly hi. No need to be shy, love awaits you here. Enjoy the enchantment!',
            'Welcome to the Find Ur Love ❤️, where sparks fly! Take a seat, open your heart, and don\'t be afraid to say hi. Love is in the air, and this is where your story begins.',
            'Enter the Find Ur Love ❤️, a sanctuary for lovebirds! Find your perfect match, make eye contact, and say hi to create a magical connection. Let love guide you on this extraordinary journey.',
            'Welcome to the Find Ur Love ❤️, where love stories unfold! Take a seat, let destiny lead the way. Don\'t hold back, say hi, and let the magic of love embrace you in this enchanting space.',
            'Step into the Find Ur Love ❤️, where love finds its voice! Settle in, seize the moment, and greet someone with a warm hi. Embrace the possibilities and let love weave its beautiful tapestry.',
            ]
            rwm = random.choice(wm)
            await self.highrise.send_whisper(user.id, f"Hey @{user.username}\n{rwm}")
            await self.highrise.send_whisper(user.id, f"\n[📢] Use !help or -help for commands. Express gratitude and support by tipping the Jar!\n\n~ Code by @OGToxic")
            face = ["FrontRight","FrontLeft"]
            fp = random.choice(face)
            _ = [Position(0.5, 1.25, 29.5, fp),Position(10.5, 1.25, 22.5, fp),Position(6.5, 1.0, 19.5, fp),Position(7.5, 1.25, 11.5, fp),Position(14.5, 7.25, 3.5, fp),Position(14.5, 7.0, 17.5, fp),Position(0.5, 7.0, 3.5, fp),Position(14.5, 7.0, 28.5, fp),Position(1.5, 14.5, 3.5, fp),Position(14.5, 14.5, 3.5, fp),Position(14.5, 14.5, 16.5, fp),Position(14.5, 14.5, 28.5, fp),]
            __ = random.choice(_)
            await self.highrise.teleport(user.id, __)
        except Exception as e:
            print(f"error : {e}")
            
    async def on_chat(self, user: User, message: str):
        try:
            _bid = "6448f9d57e36fb8bb4e65cb6"
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"
            _rid = "64243855bf25fe0e8301bef6"

            if message.lower().lstrip().startswith(("-", "!")):
                await self.command_handler(user, message)        

            if message.lower().lstrip().startswith(("!invite", "-invite")):
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, "\nUsage: !invite <@username> or -invite <@username> This command will send room invite to targeted username. if they ever interact with our bot in past\n • Example: !invite @OGToxic")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
                    return

                url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
                response = requests.get(url)
                data = response.json()
                users = data['users']
                
                for user in users:
                    user_id = user['user_id']
                    __id = f"1_on_1:{_bid}:{user_id}"
                    __idx = f"1_on_1:{user_id}:{_bid}"
                    __rid = "64243855bf25fe0e8301bef6"
                    try:
                        await self.highrise.send_message(__id, "Join Room", "invite", __rid)
                    except:
                        await self.highrise.send_message(__idx, "Join Room", "invite", __rid)

            if message.lower().lstrip().startswith(("-help", "!help")):
                await self.highrise.chat(f"\nHere are some commands:\n • !emote or -emote\n • !invite or -invite\n • !feedback\n • couple/friendly command\n   !flirt @username\n   !fight @username \n   !rock @username\n   Example : !flirt @OGToxic\n\nLeave a message to @ogtoxic for any further assistance.")

            if message.lower().lstrip().startswith("!feedback"):
                try:
                    await self.highrise.send_message(_id, "• [ Submit Feedback ]\nThank you for joining our room! We value your feedback. Please share your feedback/suggestions with @ogtoxic to enhance our environment. Your input is valuable and will help us improve.\n\nHave a wonderful day/night!", "text")
                except:
                    await self.highrise.send_message(_idx, "• [ Submit Feedback ]\nThank you for joining our room! We value your feedback. Please share your feedback/suggestions with @ogtoxic to enhance our environment. Your input is valuable and will help us improve.\n\nHave a wonderful day/night!", "text")
                    
            if message.lower().lstrip().startswith(("-emote", "!emote")):
                await self.highrise.send_whisper(user.id, "\nEmote can be used with just typing EMOTE NAME in our room. Here's an example of emote use\n  casual\n  fashionista\n  floating\n\nand all other emotes just say name in room of any emote")
                await self.highrise.send_whisper(user.id, "\n• Note that these commands will only work in room called Find Ur Love ❤️ by @OGToxic. some emotes may not work due to restrictions.")

            if message.lower().strip() == "lambipose":
                await self.highrise.send_emote("emote-superpose", user.id)
            elif message.lower().strip() == "shuffledance":
                await self.highrise.send_emote("dance-tiktok10", user.id)
            elif message.lower().strip() == "gravedance":
                await self.highrise.send_emote("dance-weird", user.id)
            elif message.lower().strip() == "fighter":
                await self.highrise.send_emote("idle-fighter", user.id)
            elif message.lower().strip() == "renegade":
                await self.highrise.send_emote("idle-dance-tiktok7", user.id)
            elif message.lower().strip() == "singalong":
                await self.highrise.send_emote("idle_singing", user.id)
            elif message.lower().strip() == "froggiehop":
                await self.highrise.send_emote("emote-frog", user.id)
            elif message.lower().strip() == "viralgroove":
                await self.highrise.send_emote("dance-tiktok9", user.id)
            elif message.lower().strip() == "swordfight":
                await self.highrise.send_emote("emote-swordfight", user.id)
            elif message.lower().strip() == "energyball":
                await self.highrise.send_emote("emote-energyball", user.id)
            elif message.lower().strip() == "emotecute":
                await self.highrise.send_emote("emote-cute", user.id)
            elif message.lower().strip() == "floating":
                await self.highrise.send_emote("emote-float", user.id)
            elif message.lower().strip() == "teleport":
                await self.highrise.send_emote("emote-teleporting", user.id)
            elif message.lower().strip() == "telekinesis":
                await self.highrise.send_emote("emote-telekinesis", user.id)
            elif message.lower().strip() == "maniac":
                await self.highrise.send_emote("emote-maniac", user.id)
            elif message.lower().strip() == "embarrassed":
                await self.highrise.send_emote("emote-embarrassed", user.id)
            elif message.lower().strip() == "pissedoff":
                await self.highrise.send_emote("emote-frustrated", user.id)
            elif message.lower().strip() == "slap":
                await self.highrise.send_emote("emote-slap", user.id)
            elif message.lower().strip() == "dotheworm":
                await self.highrise.send_emote("emote-snake", user.id)
            elif message.lower().strip() == "enthused":
                await self.highrise.send_emote("idle-enthusiastic", user.id)
            elif message.lower().strip() == "confusion":
                await self.highrise.send_emote("emote-confused", user.id)
            elif message.lower().strip() == "shopping":
                await self.highrise.send_emote("dance-shoppingcart", user.id)
            elif message.lower().strip() == "roll":
                await self.highrise.send_emote("emote-roll", user.id)
            elif message.lower().strip() == "rofl":
                await self.highrise.send_emote("emote-rofl", user.id)
            elif message.lower().strip() == "superpunch":
                await self.highrise.send_emote("emote-superpunch", user.id)
            elif message.lower().strip() == "superrun":
                await self.highrise.send_emote("emote-superrun", user.id)
            elif message.lower().strip() == "superkick":
                await self.highrise.send_emote("emote-kicking", user.id)
            elif message.lower().strip() == "zombiedance":
                await self.highrise.send_emote("dance-zombie", user.id)
            elif message.lower().strip() == "monsterfail":
                await self.highrise.send_emote("emote-monster_fail", user.id)
            elif message.lower().strip() == "peekaboo":
                await self.highrise.send_emote("emote-peekaboo", user.id)
            elif message.lower().strip() == "sumofight":
                await self.highrise.send_emote("emote-sumo", user.id)
            elif message.lower().strip() == "charging":
                await self.highrise.send_emote("emote-charging", user.id)
            elif message.lower().strip() == "ninjarun":
                await self.highrise.send_emote("emote-ninjarun", user.id)
            elif message.lower().strip() == "proposing":
                await self.highrise.send_emote("emote-proposing", user.id)
            elif message.lower().strip() == "ropepull":
                await self.highrise.send_emote("emote-ropepull", user.id)
            elif message.lower().strip() == "secrethandshake":
                await self.highrise.send_emote("emote-secrethandshake", user.id)
            elif message.lower().strip() == "elbowbump":
                await self.highrise.send_emote("emote-elbowbump", user.id)
            elif message.lower().strip() == "homerun":
                await self.highrise.send_emote("emote-baseball", user.id)
            elif message.lower().strip() == "relaxing":
                await self.highrise.send_emote("idle-floorsleeping2", user.id)
            elif message.lower().strip() == "partnerhug":
                await self.highrise.send_emote("emote-hug", user.id)
            elif message.lower().strip() == "cozynap":
                await self.highrise.send_emote("idle-floorsleeping", user.id)
            elif message.lower().strip() == "hugyourself":
                await self.highrise.send_emote("emote-hugyourself", user.id)
            elif message.lower().strip() == "snowballfight":
                await self.highrise.send_emote("emote-snowball", user.id)
            elif message.lower().strip() == "sweating":
                await self.highrise.send_emote("emote-hot", user.id)
            elif message.lower().strip() == "levelup":
                await self.highrise.send_emote("emote-levelup", user.id)
            elif message.lower().strip() == "snowangel":
                await self.highrise.send_emote("emote-snowangel", user.id)
            elif message.lower().strip() == "posh":
                await self.highrise.send_emote("idle-posh", user.id)
            elif message.lower().strip() == "fallingapart":
                await self.highrise.send_emote("emote-apart", user.id)
            elif message.lower().strip() == "poutyface":
                await self.highrise.send_emote("idle-sad", user.id)
            elif message.lower().strip() == "Irritated":
                await self.highrise.send_emote("idle-angry", user.id)
            elif message.lower().strip() == "heroentrance":
                await self.highrise.send_emote("emote-hero", user.id)
            elif message.lower().strip() == "heropose":
                await self.highrise.send_emote("idle-hero", user.id)
            elif message.lower().strip() == "russiandance":
                await self.highrise.send_emote("dance-russian", user.id)
            elif message.lower().strip() == "curtsy":
                await self.highrise.send_emote("emote-curtsy", user.id)
            elif message.lower().strip() == "bow":
                await self.highrise.send_emote("emote-bow", user.id)
            elif message.lower().strip() == "ponder":
                await self.highrise.send_emote("idle-lookup", user.id)
            elif message.lower().strip() == "headball":
                await self.highrise.send_emote("emote-headball", user.id)
            elif message.lower().strip() == "clumsy":
                await self.highrise.send_emote("emote-fail2", user.id)
            elif message.lower().strip() == "fall":
                await self.highrise.send_emote("emote-fail1", user.id)
            elif message.lower().strip() == "penny":
                await self.highrise.send_emote("dance-pennywise", user.id)
            elif message.lower().strip() == "boo":
                await self.highrise.send_emote("emote-boo", user.id)
            elif message.lower().strip() == "fly":
                await self.highrise.send_emote("emote-wings", user.id)
            elif message.lower().strip() == "floss":
                await self.highrise.send_emote("dance-floss", user.id)
            elif message.lower().strip() == "kpop":
                await self.highrise.send_emote("dance-blackpink", user.id)
            elif message.lower().strip() == "model":
                await self.highrise.send_emote("emote-model", user.id)
            elif message.lower().strip() == "theatrical":
                await self.highrise.send_emote("emote-theatrical", user.id)
            elif message.lower().strip() == "amused":
                await self.highrise.send_emote("emote-laughing2", user.id)
            elif message.lower().strip() == "jetpack":
                await self.highrise.send_emote("emote-jetpack", user.id)
            elif message.lower().strip() == "bunnyhop":
                await self.highrise.send_emote("emote-bunnyhop", user.id)
            elif message.lower().strip() == "zombie":
                await self.highrise.send_emote("Idle_zombie", user.id)
            elif message.lower().strip() == "collapse":
                await self.highrise.send_emote("emote-death2", user.id)
            elif message.lower().strip() == "revival":
                await self.highrise.send_emote("emote-death", user.id)
            elif message.lower().strip() == "disco":
                await self.highrise.send_emote("emote-disco", user.id)
            elif message.lower().strip() == "relaxed":
                await self.highrise.send_emote("idle_layingdown2", user.id)
            elif message.lower().strip() == "attentive":
                await self.highrise.send_emote("idle_layingdown", user.id)
            elif message.lower().strip() == "faint":
                await self.highrise.send_emote("emote-faint", user.id)
            elif message.lower().strip() == "cold":
                await self.highrise.send_emote("emote-cold", user.id)
            elif message.lower().strip() == "sleepy":
                await self.highrise.send_emote("idle-sleep", user.id)
            elif message.lower().strip() == "handstand":
                await self.highrise.send_emote("emote-handstand", user.id)
            elif message.lower().strip() == "ghostfloat":
                await self.highrise.send_emote("emote-ghost-idle", user.id)
            elif message.lower().strip() == "ghost":
                await self.highrise.send_emote("emoji-ghost", user.id)
            elif message.lower().strip() == "splitsdrop":
                await self.highrise.send_emote("emote-splitsdrop", user.id)
            elif message.lower().strip() == "yogaflow":
                await self.highrise.send_emote("dance-spiritual", user.id)
            elif message.lower().strip() == "smoothwalk":
                await self.highrise.send_emote("dance-smoothwalk", user.id)
            elif message.lower().strip() == "ringonit":
                await self.highrise.send_emote("dance-singleladies", user.id)
            elif message.lower().strip() == "sick":
                await self.highrise.send_emote("emoji-sick", user.id)
            elif message.lower().strip() == "wiggledance":
                await self.highrise.send_emote("dance-sexy", user.id)
            elif message.lower().strip() == "robotic":
                await self.highrise.send_emote("dance-robotic", user.id)
            elif message.lower().strip() == "naughty":
                await self.highrise.send_emote("emoji-naughty", user.id)
            elif message.lower().strip() == "pray":
                await self.highrise.send_emote("emoji-pray", user.id)
            elif message.lower().strip() == "duckwalk":
                await self.highrise.send_emote("dance-duckwalk", user.id)
            elif message.lower().strip() == "faintdrop":
                await self.highrise.send_emote("emote-deathdrop", user.id)
            elif message.lower().strip() == "voguehands":
                await self.highrise.send_emote("dance-voguehands", user.id)
            elif message.lower().strip() == "orangejuicedance":
                await self.highrise.send_emote("dance-orangejustice", user.id)
            elif message.lower().strip() == "savagedance":
                await self.highrise.send_emote("dance-tiktok8", user.id)
            elif message.lower().strip() == "hearthands":
                await self.highrise.send_emote("emote-heartfingers", user.id)
            elif message.lower().strip() == "partnerheartarms":
                await self.highrise.send_emote("emote-heartshape", user.id)
            elif message.lower().strip() == "levitate":
                await self.highrise.send_emote("emoji-halo", user.id)
            elif message.lower().strip() == "sneeze":
                await self.highrise.send_emote("emoji-sneeze", user.id)
            elif message.lower().strip() == "donot":
                await self.highrise.send_emote("dance-tiktok2", user.id)
            elif message.lower().strip() == "rockout":
                await self.highrise.send_emote("dance-metal", user.id)
            elif message.lower().strip() == "pushups":
                await self.highrise.send_emote("dance-aerobics", user.id)
            elif message.lower().strip() == "karate":
                await self.highrise.send_emote("dance-martial-artist", user.id)
            elif message.lower().strip() == "macarena":
                await self.highrise.send_emote("dance-macarena", user.id)
            elif message.lower().strip() == "handsintheair":
                await self.highrise.send_emote("dance-handsup", user.id)
            elif message.lower().strip() == "breakdance":
                await self.highrise.send_emote("dance-breakdance", user.id)
            elif message.lower().strip() == "fireballlunge":
                await self.highrise.send_emote("emoji-hadoken", user.id)
            elif message.lower().strip() == "arrogance":
                await self.highrise.send_emote("emoji-arrogance", user.id)
            elif message.lower().strip() == "smirk":
                await self.highrise.send_emote("emoji-smirking", user.id)
            elif message.lower().strip() == "lying":
                await self.highrise.send_emote("emoji-lying", user.id)
            elif message.lower().strip() == "giveup":
                await self.highrise.send_emote("emoji-give-up", user.id)
            elif message.lower().strip() == "punch":
                await self.highrise.send_emote("emoji-punch", user.id)
            elif message.lower().strip() == "stinky":
                await self.highrise.send_emote("emoji-poop", user.id)
            elif message.lower().strip() == "point":
                await self.highrise.send_emote("emoji-there", user.id)
            elif message.lower().strip() == "annoyed":
                await self.highrise.send_emote("idle-loop-annoyed", user.id)
            elif message.lower().strip() == "taploop":
                await self.highrise.send_emote("idle-loop-tapdance", user.id)
            elif message.lower().strip() == "bummed":
                await self.highrise.send_emote("idle-loop-sad", user.id)
            elif message.lower().strip() == "chillin":
                await self.highrise.send_emote("idle-loop-happy", user.id)
            elif message.lower().strip() == "aerobics":
                await self.highrise.send_emote("idle-loop-aerobics", user.id)
            elif message.lower().strip() == "boogieswing":
                await self.highrise.send_emote("idle-dance-swinging", user.id)
            elif message.lower().strip() == "think":
                await self.highrise.send_emote("emote-think", user.id)
            elif message.lower().strip() == "blastoff":
                await self.highrise.send_emote("emote-disappear", user.id)
            elif message.lower().strip() == "gasp":
                await self.highrise.send_emote("emoji-scared", user.id)
            elif message.lower().strip() == "eyeroll":
                await self.highrise.send_emote("emoji-eyeroll", user.id)
            elif message.lower().strip() == "sob":
                await self.highrise.send_emote("emoji-crying", user.id)
            elif message.lower().strip() == "frolic":
                await self.highrise.send_emote("emote-frollicking", user.id)
            elif message.lower().strip() == "graceful":
                await self.highrise.send_emote("emote-graceful", user.id)
            elif message.lower().strip() == "rest":
                await self.highrise.send_emote("sit-idle-cute", user.id)
            elif message.lower().strip() == "greedyemote":
                await self.highrise.send_emote("emote-greedy", user.id)
            elif message.lower().strip() == "flirtywave":
                await self.highrise.send_emote("emote-lust", user.id)
            elif message.lower().strip() == "tiredx":
                await self.highrise.send_emote("idle-loop-tired", user.id)
            elif message.lower().strip() == "tummyache":
                await self.highrise.send_emote("emoji-gagging", user.id)
            elif message.lower().strip() == "flex":
                await self.highrise.send_emote("emoji-flex", user.id)
            elif message.lower().strip() == "raisetheroof":
                await self.highrise.send_emote("emoji-celebrate", user.id)
            elif message.lower().strip() == "cursingemote":
                await self.highrise.send_emote("emoji-cursing", user.id)
            elif message.lower().strip() == "stunned":
                await self.highrise.send_emote("emoji-dizzy", user.id)
            elif message.lower().strip() == "mindblown":
                await self.highrise.send_emote("emote-mindblown", user.id)
            elif message.lower().strip() == "shy":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "sit":
                await self.highrise.send_emote("idle-loop-sitfloor", user.id)
            elif message.lower().strip() == "thumbsup":
                await self.highrise.send_emote("emote-thumbsup", user.id)
            elif message.lower().strip() == "clap":
                await self.highrise.send_emote("emote-clap", user.id)
            elif message.lower().strip() == "angry":
                await self.highrise.send_emote("emote-mad", user.id)
            elif message.lower().strip() == "tired":
                await self.highrise.send_emote("emote-sleepy", user.id)
            elif message.lower().strip() == "thewave":
                await self.highrise.send_emote("emote-thewave", user.id)
            elif message.lower().strip() == "thumbsuck":
                await self.highrise.send_emote("emote-suckthumb", user.id)
            elif message.lower().strip() == "shy":
                await self.highrise.send_emote("idle-loop-shy", user.id)
            elif message.lower().strip() == "peace":
                await self.highrise.send_emote("emote-peace", user.id)
            elif message.lower().strip() == "panic":
                await self.highrise.send_emote("emote-panic", user.id)
            elif message.lower().strip() == "jump":
                await self.highrise.send_emote("emote-jumpb", user.id)
            elif message.lower().strip() == "loveflutter":
                await self.highrise.send_emote("emote-hearteyes", user.id)
            elif message.lower().strip() == "exasperated":
                await self.highrise.send_emote("emote-exasperated", user.id)
            elif message.lower().strip() == "facepalm":
                await self.highrise.send_emote("emote-exasperatedb", user.id)
            elif message.lower().strip() == "dab":
                await self.highrise.send_emote("emote-dab", user.id)
            elif message.lower().strip() == "gangnamstyle":
                await self.highrise.send_emote("emote-gangnam", user.id)
            elif message.lower().strip() == "harlemshake":
                await self.highrise.send_emote("emote-harlemshake", user.id)
            elif message.lower().strip() == "tapdance":
                await self.highrise.send_emote("emote-tapdance", user.id)
            elif message.lower().strip() == "yes":
                await self.highrise.send_emote("emote-yes", user.id)
            elif message.lower().strip() == "sad":
                await self.highrise.send_emote("emote-sad", user.id)
            elif message.lower().strip() == "robot":
                await self.highrise.send_emote("emote-robot", user.id)
            elif message.lower().strip() == "rainbow":
                await self.highrise.send_emote("emote-rainbow", user.id)
            elif message.lower().strip() == "no":
                await self.highrise.send_emote("emote-no", user.id)
            elif message.lower().strip() == "nightfever":
                await self.highrise.send_emote("emote-nightfever", user.id)
            elif message.lower().strip() == "laugh":
                await self.highrise.send_emote("emote-laughing", user.id)
            elif message.lower().strip() == "kiss":
                await self.highrise.send_emote("emote-kiss", user.id)
            elif message.lower().strip() == "judochop":
                await self.highrise.send_emote("emote-judochop", user.id)
            elif message.lower().strip() == "hello":
                await self.highrise.send_emote("emote-hello", user.id)
            elif message.lower().strip() == "happy":
                await self.highrise.send_emote("emote-happy", user.id)
            elif message.lower().strip() == "moonwalk":
                await self.highrise.send_emote("emote-gordonshuffle", user.id)
            elif message.lower().strip() == "zombierun":
                await self.highrise.send_emote("emote-zombierun", user.id)
            elif message.lower().strip() == "cheerful":
                await self.highrise.send_emote("emote-pose8", user.id)
            elif message.lower().strip() == "embracingmodel":
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "embracing":
                await self.highrise.send_emote("emote-pose7", user.id)
            elif message.lower().strip() == "fashionpose":
                await self.highrise.send_emote("emote-pose5", user.id)
            elif message.lower().strip() == "fashion":
                await self.highrise.send_emote("emote-pose5", user.id)
            elif message.lower().strip() == "ichallengeyou":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "challenge":
                await self.highrise.send_emote("emote-pose3", user.id)
            elif message.lower().strip() == "flirtywink":
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.lower().strip() == "wink":
                await self.highrise.send_emote("emote-pose1", user.id)
            elif message.lower().strip() == "acasualdance":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "casualdance":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "casual":
                await self.highrise.send_emote("idle-dance-casual", user.id)
            elif message.lower().strip() == "cutie":
                await self.highrise.send_emote("emote-cutey", user.id)
            elif message.lower().strip() == "zerogravity":
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.lower().strip() == "zerogravity":
                await self.highrise.send_emote("emote-astronaut", user.id)
            elif message.lower().strip() == "saysodance":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "sodance":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "saydance":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "sayso":
                await self.highrise.send_emote("idle-dance-tiktok4", user.id)
            elif message.lower().strip() == "punkguitar":
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "punk":
                await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "guitar":
                 await self.highrise.send_emote("emote-punkguitar", user.id)
            elif message.lower().strip() == "icecream":
                await self.highrise.send_emote("dance-icecream", user.id)
            elif message.lower().strip() == "gravity":
                await self.highrise.send_emote("emote-gravity", user.id)
            elif message.lower().strip() == "fashionista":
                await self.highrise.send_emote("emote-fashionista", user.id)
            elif message.lower().strip() == "uwu":
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.lower().strip() == "uwumood":
                await self.highrise.send_emote("idle-uwu", user.id)
            elif message.lower().strip() == "wrong":
                await self.highrise.send_emote("dance-wrong", user.id)
            elif message.lower().strip() == "dancewrong":
                await self.highrise.send_emote("dance-wrong", user.id)                

            blacklisted_words = ["2 girls 1 cup", "2g1c", "4r5e", "5h1t", "5hit", "a55", "a_s_s", "acrotomophilia", "alabama hot pocket", "alaskan pipeline", "anal", "anilingus", "anus", "apeshit", "ar5e", "arrse", "arse", "arsehole", "ass", "ass-fucker", "ass-hat", "ass-pirate", "assbag", "assbandit", "assbanger", "assbite", "assclown", "asscock", "asscracker", "asses", "assface", "assfucker", "assfukka", "assgoblin", "asshat", "asshead", "asshole", "assholes", "asshopper", "assjacker", "asslick", "asslicker", "assmonkey", "assmunch", "assmuncher", "asspirate", "assshole", "asssucker", "asswad", "asswhole", "asswipe", "auto erotic", "autoerotic", "b!tch", "b00bs", "b17ch", "b1tch", "babeland", "baby batter", "baby juice", "ball gag", "ball gravy", "ball kicking", "ball licking", "ball sack", "ball sucking", "ballbag", "balls", "ballsack", "bampot", "bangbros", "bareback", "barely legal", "barenaked", "bastard", "bastardo", "bastinado", "bbw", "bdsm", "beaner", "beaners", "beastial", "beastiality", "beastility", "beaver cleaver", "beaver lips", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "big black", "big breasts", "big knockers", "big tits", "bimbos", "birdlock", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "black cock", "blonde action", "blonde on blonde action", "bloody", "blow job", "blow your load", "blowjob", "blowjobs", "blue waffle", "blumpkin", "boiolas", "bollock", "bollocks", "bollok", "bollox", "bondage", "boner", "boob", "boobie", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "booty call", "breasts", "brown showers", "brunette action", "buceta", "bugger", "bukkake", "bulldyke", "bullet vibe", "bullshit", "bum", "bung hole", "bunghole", "bunny fucker", "busty", "butt", "butt-pirate", "buttcheeks", "butthole", "buttmunch", "buttplug", "c0ck", "c0cksucker", "camel toe", "camgirl", "camslut", "camwhore", "carpet muncher", "carpetmuncher", "cawk", "chinc", "chink", "choad", "chocolate rosebuds", "chode", "cipa", "circlejerk", "cl1t", "cleveland steamer", "clit", "clitface", "clitoris", "clits", "clover clamps", "clusterfuck", "cnut", "cock", "cock-sucker", "cockbite", "cockburger", "cockface", "cockhead", "cockjockey", "cockknoker", "cockmaster", "cockmongler", "cockmongruel", "cockmonkey", "cockmunch", "cockmuncher", "cocknose", "cocknugget", "cocks", "cockshit", "cocksmith", "cocksmoker", "cocksuck", "cocksuck ", "cocksucked", "cocksucked ", "cocksucker", "cocksucking", "cocksucks ", "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coochie", "coochy", "coon", "coons", "cooter", "coprolagnia", "coprophilia", "cornhole", "cox", "crap", "creampie", "cum", "cumbubble", "cumdumpster", "cumguzzler", "cumjockey", "cummer", "cumming", "cums", "cumshot", "cumslut", "cumtart", "cunilingus", "cunillingus", "cunnie", "cunnilingus", "cunt", "cuntface", "cunthole", "cuntlick", "cuntlick ", "cuntlicker", "cuntlicker ", "cuntlicking", "cuntlicking ", "cuntrag", "cunts", "cyalis", "cyberfuc", "cyberfuck ", "cyberfucked ", "cyberfucker", "cyberfuckers", "cyberfucking ", "d1ck", "dammit", "damn", "darkie", "date rape", "daterape", "deep throat", "deepthroat", "dendrophilia", "dick", "dickbag", "dickbeater", "dickface", "dickhead", "dickhole", "dickjuice", "dickmilk", "dickmonger", "dickslap", "dicksucker", "dickwad", "dickweasel", "dickweed", "dickwod", "dike", "dildo", "dildos", "dingleberries", "dingleberry", "dink", "dinks", "dipshit", "dirsa", "dirty pillows", "dirty sanchez", "dlck", "dog style", "dog-fucker", "doggie style", "doggiestyle", "doggin", "dogging", "doggy style", "doggystyle", "dolcett", "domination", "dominatrix", "dommes", "donkey punch", "donkeyribber", "doochbag", "dookie", "doosh", "double dong", "double penetration", "douche", "douchebag", "dp action", "dry hump", "duche", "dumbshit", "dumshit", "dvda", "dyke", "eat my ass", "ecchi", "ejaculate", "ejaculated", "ejaculates ", "ejaculating ", "ejaculatings", "ejaculation", "ejakulate", "erotic", "erotism", "escort", "eunuch", "f u c k", "f u c k e r", "f4nny", "f_u_c_k", "fag", "fagbag", "fagg", "fagging", "faggit", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fagtard", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fart", "farted", "farting", "farty", "fatass", "fcuk", "fcuker", "fcuking", "fecal", "feck", "fecker", "felatio", "felch", "felching", "fellate", "fellatio", "feltch", "female squirting", "femdom", "figging", "fingerbang", "fingerfuck ", "fingerfucked ", "fingerfucker ", "fingerfuckers", "fingerfucking ", "fingerfucks ", "fingering", "fistfuck", "fistfucked ", "fistfucker ", "fistfuckers ", "fistfucking ", "fistfuckings ", "fistfucks ", "fisting", "flamer", "flange", "fook", "fooker", "foot fetish", "footjob", "frotting", "fuck", "fuck buttons", "fucka", "fucked", "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme ", "fucks", "fucktards", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "futanari", "fux", "fux0r", "g-spot", "gang bang", "gangbang", "gangbanged", "gangbanged ", "gangbangs ", "gay sex", "gayass", "gaybob", "gaydo", "gaylord", "gaysex", "gaytard", "gaywad", "genitals", "giant cock", "girl on", "girl on top", "girls gone wild", "goatcx", "goatse", "god damn", "god-dam", "god-damned", "goddamn", "goddamned", "gokkun", "golden shower", "goo girl", "gooch", "goodpoop", "gook", "goregasm", "gringo", "grope", "group sex", "guido", "guro", "hand job", "handjob", "hard core", "hardcore", "hardcoresex ", "heeb", "hell", "hentai", "heshe", "ho", "hoar", "hoare", "hoe", "hoer", "homo", "homoerotic", "honkey", "honky", "hooker", "hore", "horniest", "horny", "hot carl", "hot chick", "hotsex", "how to kill", "how to murder", "huge fat", "humping", "incest", "intercourse", "jack off", "jack-off ", "jackass", "jackoff", "jail bait", "jailbait", "jap", "jelly donut", "jerk off", "jerk-off ", "jigaboo", "jiggaboo", "jiggerboo", "jism", "jiz", "jiz ", "jizm", "jizm ", "jizz", "juggs", "kawk", "kike", "kinbaku", "kinkster", "kinky", "kiunt", "knob", "knobbing", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums", "kooch", "kootch", "kum", "kumer", "kummer", "kumming", "kums", "kunilingus", "kunt", "kyke", "l3i+ch", "l3itch", "labia", "leather restraint", "leather straight jacket", "lemon party", "lesbo", "lezzie", "lmfao", "lolita", "lovemaking", "lust", "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "make me come", "male squirting", "masochist", "master-bate", "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "menage a trois", "milf", "minge", "missionary position", "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked ", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking ", "mothafuckings", "mothafucks", "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "mound of venus", "mr hands", "muff", "muff diver", "muffdiver", "muffdiving", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nambla", "nawashi", "nazi", "negro", "neonazi", "nig nog", "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers ", "niglet", "nimphomania", "nipple", "nipples", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", "nsfw images", "nude", "nudity", "numbnuts", "nutsack", "nympho", "nymphomania", "octopussy", "omorashi", "one cup two girls", "one guy one jar", "orgasim", "orgasim ", "orgasims ", "orgasm", "orgasms ", "orgy", "p0rn", "paedophile", "paki", "panooch", "panties", "panty", "pawn", "pecker", "peckerhead", "pedobear", "pedophile", "pegging", "penis", "penisfucker", "phone sex", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "piece of shit", "pigfucker", "pimpis", "pis", "pises", "pisin", "pising", "pisof", "piss", "piss pig", "pissed", "pisser", "pissers", "pisses ", "pissflap", "pissflaps", "pissin", "pissin ", "pissing", "pissoff", "pissoff ", "pisspig", "playboy", "pleasure chest", "pole smoker", "polesmoker", "pollock", "ponyplay", "poo", "poof", "poon", "poonani", "poonany", "poontang", "poop", "poop chute", "poopchute", "porn", "porno", "pornography", "pornos", "prick", "pricks ", "prince albert piercing", "pron", "pthc", "pube", "pubes", "punanny", "punany", "punta", "pusies", "pusse", "pussi", "pussies", "pussy", "pussylicking", "pussys ", "pusy", "puto", "queaf", "queef", "queerbait", "queerhole", "quim", "raghead", "raging boner", "rape", "raping", "rapist", "rectum", "renob", "retard", "reverse cowgirl", "rimjaw", "rimjob", "rimming", "rosy palm", "rosy palm and her 5 sisters", "ruski", "rusty trombone", "s hit", "s&m", "s.o.b.", "s_h_i_t", "sadism", "sadist", "santorum", "scat", "schlong", "scissoring", "screwing", "scroat", "scrote", "scrotum", "semen", "sex", "sexo", "sexy", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shaved beaver", "shaved pussy", "shemale", "shi+", "shibari", "shit", "shit-ass", "shit-bag", "shit-bagger", "shit-brain", "shit-breath", "shit-cunt", "shit-dick", "shit-eating", "shit-face", "shit-faced", "shit-fit", "shit-head", "shit-heel", "shit-hole", "shit-house", "shit-load", "shit-pot", "shit-spitter", "shit-stain", "shitass", "shitbag", "shitbagger", "shitblimp", "shitbrain", "shitbreath", "shitcunt", "shitdick", "shite", "shiteating", "shited", "shitey", "shitface", "shitfaced", "shitfit", "shitfuck", "shitfull", "shithead", "shitheel", "shithole", "shithouse", "shiting", "shitings", "shitload", "shitpot", "shits", "shitspitter", "shitstain", "shitted", "shitter", "shitters ", "shittiest", "shitting", "shittings", "shitty", "shitty ", "shity", "shiz", "shiznit", "shota", "shrimping", "skank", "skeet", "slanteye", "slut", "slutbag", "sluts", "smeg", "smegma", "smut", "snatch", "snowballing", "sodomize", "sodomy", "son-of-a-bitch", "spac", "spic", "spick", "splooge", "splooge moose", "spooge", "spread legs", "spunk", "strap on", "strapon", "strappado", "strip club", "style doggy", "suck", "sucks", "suicide girls", "sultry women", "swastika", "swinger", "t1tt1e5", "t1tties", "tainted love", "tard", "taste my", "tea bagging", "teets", "teez", "testical", "testicle", "threesome", "throating", "thundercunt", "tied up", "tight white", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties", "titty", "tittyfuck", "tittywank", "titwank", "tongue in a", "topless", "tosser", "towelhead", "tranny", "tribadism", "tub girl", "tubgirl", "turd", "tushy", "tw4t", "twat", "twathead", "twatlips", "twatty", "twink", "twinkie", "two girls one cup", "twunt", "twunter", "undressing", "upskirt", "urethra play", "urophilia", "v14gra", "v1gra", "va-j-j", "vag", "vagina", "venus mound", "viagra", "vibrator", "violet wand", "vjayjay", "vorarephilia", "voyeur", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "wet dream", "wetback", "white power", "whoar", "whore", "willies", "willy", "wrapping men", "wrinkled starfish", "xrated", "xx", "xxx", "yaoi", "yellow showers", "yiffy", "zoophilia"]
            if user.id not in user_warnings:
                user_warnings[user.id] = 0

            try:
                for word in blacklisted_words:
                    if word in message.lower():
                        user_warnings[user.id] += 1
                        censored_word = word[0] + '*' * (len(word) - 2) + word[-1]
                        if user_warnings[user.id] == 2:
                            await self.highrise.send_whisper(user.id, f"\nMuted For 60 Seconds, Because Of Word: {censored_word}")
                            await self.highrise.moderate_room(user.id, "mute", 60)
                        elif user_warnings[user.id] >= 3:
                            await self.highrise.send_whisper(user.id, f"\nMuted For 10 Mins, Because Of Word: {censored_word}")
                            await self.highrise.moderate_room(user.id, "mute", 360)
                        else:
                            await self.highrise.chat(f"\nHey @{user.username}! It seems your message included inappropriate language. Let's maintain a respectful environment. Please avoid using such words in the future. Thanks! 🙏\n\n • username : @{user.username}\n • word : {censored_word}\n • Possible actions : mute/ban/kick")
                            await self.highrise.send_whisper(user.id, f"\nHey @{user.username}! It seems your message included inappropriate language. Let's maintain a respectful environment. Please avoid using such words in the future. Thanks! 🙏\n\n • word : {censored_word}\n • Possible actions : mute/ban/kick")
                        break
            except Exception as e:
                print(f"An exception occurred[BlackList-Words]: {e}")

        except Exception as e:
            print(f"error : {e}")
        
    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "handlers/mods"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        return

    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)

#keep_alive()
if __name__ == "__main__":
    room_id = "64243855bf25fe0e8301bef6"
    token = "2b60f534bed1a2ae7e79262ac7a3fd734495cc600261be25daba5545f27e516c"
    arun(Bot().run(room_id, token))
