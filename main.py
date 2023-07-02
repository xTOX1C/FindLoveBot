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
import random
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class Bot(BaseBot):
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        print("Alive!")
        await self.highrise.walk_to(Position(16.5, 1.25, 12.5, "FrontLeft"))
        await self.highrise.chat("Hey I'm Back! Sorry For Inconvenience")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        await self.highrise.chat(f"{user.username} sent reaction {reaction} to {receiver.username}")
  
    async def on_user_join(self, user: User) -> None:
        try:
            prGreen(f"@{user.username} Joined the room")
            await self.highrise.send_whisper(user.id, f"\nHey @{user.username}! How Are You?\n\n~ Code By @OGToxic")
            await self.highrise.send_whisper(user.id, "\nType emotename To Use Emotes\n- Some Examples\ncasual\nicecream\ngravity\nzerogravity\nAnd All Others")
        except Exception as e:
            print(f"Error : {e}")

    async def on_chat(self, user: User, message: str):
        try:
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
            elif message.lower().strip() == "snowballfight!":
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
            elif message.lower().strip() == "imaginaryjetpack":
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
        except Exception as e:
            print(f"Error : {e}")
        
    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)

if __name__ == "__main__":
    room_id = "64243855bf25fe0e8301bef6"
    token = "730eca2b40a01ffea667042599ac95b430547d3e56b2cefb8246022224f8a8b7"
    arun(Bot().run(room_id, token))
    