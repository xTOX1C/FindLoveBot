import highrise
from highrise import*
from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
)
from highrise.models import (
    GetMessagesRequest,
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
from handlers.public.loop import ContinuousEmoteHandler
import requests
import random
import asyncio
import os
import sys
import json
import time
import importlib
user_warnings = {}
EMOTE_LIST = ["dance-jinglebell", "emote-timejump", "emote-celebrate","emote-stargazer", "emote-astronaut", "dance-pinguin", "dance-anime", "dance-creepypuppet", "emote-creepycute", "emote-shy2", "emote-pose10", "emote-punkguitar","emote-zombierun", "emote-gravity", "dance-icecream", "dance-wrong", "emote-headblowup", "idle-guitar", "dance-tiktok10", "idle_singing", "dance-tiktok9", "idle-dance-casual"]

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

class Bot(BaseBot):

    def __init__(self,  *args, **kwargs):
        super().__init__( *args, **kwargs)

        with open("mods.json", "r") as e:
           self._mods = json.load(e)                   

        with open("emote.json", "r") as f:
            self.emotes = json.load(f)

            self.continuous_emote_tasks = {} 
            self.AREA_MIN_X = 10.5
            self.AREA_MAX_X = 15.5
            self.AREA_MIN_Y = 0
            self.AREA_MAX_Y = 1.0
            self.AREA_MIN_Z = 11.5
            self.AREA_MAX_Z = 18.5
            self.user_positions = {}
            self.continuous_emote_handler = ContinuousEmoteHandler(self.emotes, self.continuous_emote_tasks)

    async def restart_program(self):
        try:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        except Exception as e:
            print(f"Error in restart: {e}")
            
    async def send_continuous_emotes(self):
        try:
            while True:
                room_users_response = await self.highrise.get_room_users()
                room_users = room_users_response.content
                emote = random.choice(EMOTE_LIST)
                emote_tasks = [self.send_emote_to_user(emote, user.id) for user, pos in room_users if self.is_user_in_specified_area(pos)]
                await asyncio.gather(*emote_tasks)
                await asyncio.sleep(9)
        except Exception as e:
            print(f"Error sending continuous emotes: {e}")
        
    async def send_emote_to_user(self, emote, user_id):
        try:
            await self.highrise.send_emote(emote, user_id)
        except highrise.ResponseError as e:
            if "Target user not in room" in str(e):
                print(f"User with ID {user_id} left the room. Skipping emote.")
            else:
                print(f"Error sending emote to user with ID {user_id}: {e}")
          
    def is_user_in_specified_area(self, pos):
        if pos is not None:
            if isinstance(pos, AnchorPosition):
                x, y, z = self.get_position_coordinates(pos)
            else:
                x, y, z = self.get_position_coordinates(pos)
                return (
                        self.AREA_MIN_X <= x <= self.AREA_MAX_X
                        and self.AREA_MIN_Y <= y <= self.AREA_MAX_Y
                        and self.AREA_MIN_Z <= z <= self.AREA_MAX_Z
                        )
        return False
    
    def get_position_coordinates(self, pos):
        if pos is not None:
            if hasattr(pos, 'x'):
                x = pos.x
            elif hasattr(pos, 'position') and hasattr(pos.position, 'x'):
                x = pos.position.x
            else:
                print(f"Unknown x coordinate type: {pos}")
                x = None
            if hasattr(pos, 'y'):
                y = pos.y
            elif hasattr(pos, 'position') and hasattr(pos.position, 'y'):
                y = pos.position.y
            else:
                print(f"Unknown y coordinate type: {pos}")
                y = None
            if hasattr(pos, 'z'):
                z = pos.z
            elif hasattr(pos, 'position') and hasattr(pos.position, 'z'):
                z = pos.position.z
            else:
                print(f"Unknown z coordinate type: {pos}")
                z = None
            return x, y, z
        return None, None, None

    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            print("alive")
    
            # Check and cancel existing task if it's running
            if hasattr(self, 'continuous_emotes_task') and not self.continuous_emotes_task.done():
                self.continuous_emotes_task.cancel()
    
            await self.highrise.walk_to(Position(16.5, 1.0, 6.5, "FrontLeft"))
            await self.highrise.chat("Reconnected...")
    
            room_users_response = await self.highrise.get_room_users()
            room_users = room_users_response.content
    
            for user, pos in room_users:
                if self.is_user_in_specified_area(pos):
                    await self.on_user_move(user, pos)
                    print(f"Initialization complete for user {user.username}.")
                else:
                    print(f"User {user.username} is not in the specified area. Skipping initialization.")
    
            # Run the new task
            self.continuous_emotes_task = asyncio.create_task(self.send_continuous_emotes())
    
            while True:
                # Check and cancel existing task if it's running for sending individual emotes
                if hasattr(self, 'send_emote_task') and not self.send_emote_task.done():
                    self.send_emote_task.cancel()
    
                random_key = random.choice(list(self.emotes.keys()))
                random_emote = self.emotes[random_key]
    
                # Run the new task for sending individual emotes
                self.send_emote_task = asyncio.create_task(self.highrise.send_emote(random_emote))
                await asyncio.sleep(10)
    
        except asyncio.CancelledError:
            # Catch the CancelledError to handle task cancellation
            print("Task canceled.")
        except Exception as e:
            print(f"error: {e}")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        text_to_emoji = {
        "wink": "😉",
        "wave": "👋",
        "thumbs": "👍",
        "heart": "❤️",
        "clap": "👏",
        }
        await self.highrise.chat(f"\n{user.username} {text_to_emoji[reaction]} {receiver.username}")

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        try:
            print(f"{user.username} Joined Room.")
            wm = [
            'Where hearts connect!',
            'Take a seat, let love find you.',
            'Don\'t hesitate to say Hi and start a conversation.',
            'Embrace the magic of connection and let your journey begin!',
            'where souls intertwine!',
            'Find your special someone and break the ice with a friendly Hi.',
            'No need to be shy, love awaits you here.',
            'Enjoy the enchantment!',
            'Where sparks fly!',
            'Take a seat, open your heart, and don\'t be afraid to say Hi.',
            'Love is in the air, and this is where your story begins.',
            'A sanctuary for lovebirds!',
            'Find your perfect match, make eye contact, and say Hi to create a magical connection.',
            'Let love guide you on this extraordinary journey.',
            'Where love stories unfold!',
            'Take a seat, let destiny lead the way.',
            'Don\'t hold back, say Hi, and let the magic of love embrace you in this enchanting space.',
            'Where love finds its voice!',
            'Settle in, seize the moment, and greet someone with a warm Hi.',
            'Embrace the possibilities and let love weave its beautiful tapestry.'
            ]
            rwm = random.choice(wm)
            await self.highrise.send_whisper(user.id, f'Hey @{user.username}\nWelcome to the Find Ur Love ❤️\n{rwm}\n\nJust say "help" for guide\n~ Code by @OGToxic')
            await self.highrise.send_whisper(user.id, f'\nTry new emotes "Gottago", "Timejump" and "Jingle"')
            face = ["FrontRight","FrontLeft"]
            fp = random.choice(face)
            _ = [Position(0.5, 1.25, 29.5, fp),Position(10.5, 1.25, 22.5, fp),Position(6.5, 1.0, 19.5, fp),Position(7.5, 1.25, 11.5, fp),Position(14.5, 7.25, 3.5, fp),Position(14.5, 7.0, 17.5, fp),Position(0.5, 7.0, 3.5, fp),Position(14.5, 7.0, 28.5, fp),Position(1.5, 14.5, 3.5, fp),Position(14.5, 14.5, 3.5, fp),Position(14.5, 14.5, 16.5, fp),Position(14.5, 14.5, 28.5, fp),]
            __ = random.choice(_)
            #await self.highrise.teleport(user.id, __)
        except Exception as e:
            print(f"error : {e}")

    async def on_whisper(self, user: User, message: str) -> None:
        try:
            _bid = "6448f9d57e36fb8bb4e65cb6"
            _uri = "644c84fc64d782bbf8721bc5"
            _id = f"1_on_1:{_bid}:{_uri}"
            _idx = f"1_on_1:{_uri}:{_bid}"
            try:
                await self.highrise.send_message(_id, f'\n~ @{user.username} Whispered "{message}"', "text")
            except:
                await self.highrise.send_message(_idx, f'\n~ @{user.username} Whispered "{message}"', "text")
            #print(f"{user.username} whispered: {message}")
        except Exception as e:
            print(f"error in whisper : {e}")

    async def on_chat(self, user: User, message: str):
        try:
            _bid = "6448f9d57e36fb8bb4e65cb6"
            _id = f"1_on_1:{_bid}:{user.id}"
            _idx = f"1_on_1:{user.id}:{_bid}"
            _rid = "64243855bf25fe0e8301bef6"
            input_emote = message.strip().lower()

            if input_emote.startswith("loop"):
                # Extract the emote name from the message
                loop_emote_name = input_emote[4:].strip()

                # Start a new loop with the specified emote
                await self.continuous_emote_handler.start_continuous_emote(self.highrise, loop_emote_name, user.id)
            elif input_emote.lower() == "stop":
                # Stop the continuous emote for the user
                await self.continuous_emote_handler.stop_continuous_emote(user.id)

            if message.lower().lstrip() == "help":
                await self.highrise.send_whisper(user.id, f"\n-loop emotename\n• Example :\n  loop enthused\n  stop ( to stop loop)\n\nemotename\nemotename @username\n• Example:\n  enthused\n  enthused @findlove")
            
            if message.lower().lstrip() == "-rf" and user.username.lower() in self._mods:
                await self.highrise.send_whisper(user.id, f"\nRestarting")
                await self.restart_program()
            
            if message.lower().strip().startswith(("!")):
                if user.username.lower() in self._mods:
                    pass
                else:
                    await self.highrise.send_whisper(user.id, f"\nHey @{user.username}, You're not allowed to use commands that starts with !")
                    return
                await self.mod_handler(user, message)
            
            _message = message.lower().strip()
            command_split = _message.split()
            emote_detect = command_split[0]
            
            if emote_detect in self.emotes and len(command_split) == 1:
                await self.highrise.send_emote(self.emotes[emote_detect], user.id)
                return
            elif emote_detect in self.emotes and len(command_split) > 1 and not command_split[1].startswith("@"):
                await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                return

            elif emote_detect in self.emotes and len(command_split) == 2:
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                user_id = next((u.id for u in users if u.username.lower() == command_split[1][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User @{command_split[1][1:]} not found")
                    return
                try:
                    await self.highrise.send_emote(self.emotes[emote_detect], user.id)
                    await self.highrise.send_emote(self.emotes[emote_detect], user_id)
                except Exception as e:
                    print(f"An exception occurred [in user 2 user emote]: {e}")
                return

            elif emote_detect in self.emotes and len(command_split) > 2:
                await self.highrise.send_whisper(user.id, '\nusage : "emotename" or "emotename @username"')
                return

            #elif emote_detect not in self.emotes:
               #await self.highrise.chat("\nEmote Not Found")

            #if message.lower().strip().startswith(("-")):
                #await self.public_handler(user, message)

            blacklisted_words = ["fuck", "nigga", "mf", "butt", "boobs", "pussy", "dick", "asshole", "ass", "shit", "sex", "hoe", "slut", "bitch", "ugly"]
            if user.id not in user_warnings:
                user_warnings[user.id] = 0

            try:
                for word in blacklisted_words:
                    if word in message.lower().split():
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

    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        try:
            response = await self.highrise.get_messages(conversation_id)
            if isinstance(response, GetMessagesRequest.GetMessagesResponse):
                message = response.messages[0].content
            print (message)

            if message.lower().lstrip() == "-rf" and user_id in self._mods:
                await self.highrise.send_message(conversation_id, "Restarting")
                await self.restart_program()
        except Exception as e:
                print(f"Error in messages : {e}")
            
    async def mod_handler(self, user: User, message: str):
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

    async def public_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "handlers/public"
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
    room_id = "6552fb4719c844f40b94297e"
    token = "2b60f534bed1a2ae7e79262ac7a3fd734495cc600261be25daba5545f27e516c"
    arun(Bot().run(room_id, token))

                          
