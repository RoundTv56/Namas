import asyncio
import contextlib
import os
import json
import importlib
import sys
from highrise import ResponseError
import contextlib
import random
import logging
import socket
from random import randrange
from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *
from ability.country import get_country_info
from ability.dance import send_continuous_emotes
from typing import Any, Dict, Union
from keep_alive import keep_alive

keep_alive()
from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
    AnchorPosition,
    BaseBot,
    Position,
    Reaction,
    ResponseError,
    User,
    CurrencyItem,
    GetMessagesRequest,
    Item,
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
db = {}
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import time
import aioconsole
 
moderators = ["iZexy"]


class Bot(BaseBot):
  continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}
  user_data: Dict[int, Dict[str, Any]] = {}
  EMOTE_DICT = {
      "charging": "emote-charging",
      "energyball": "emote-energyball",
      "fashionista": "emote-fashionista",
      "flex": "emoji-flex",
      "flirtywave": "emote-lust",
      "float": "emote-float",
      "frog": "emote-frog",
      "gravedance": "dance-weird",
      "gravity": "emote-gravity",
      "greedy": "emote-greedy",
      "hello": "emote-hello",
      "hot": "emote-hot",
      "icecream": "dance-icecream",
      "kiss": "emote-kiss",
      "kpop": "dance-blackpink",
      "lambi": "emote-superpose",
      "laugh": "emote-laughing",
      "letsgo": "dance-shoppingcart",
      "maniac": "emote-maniac",
      "model": "emote-model",
      "no": "emote-no",
      "ogdance": "dance-macarena",
      "pennydance": "dance-pennywise",
      "pose1": "emote-pose1",
      "pose2": "emote-pose3",
      "pose3": "emote-pose5",
      "pose4": "emote-pose7",
      "pose5": "emote-pose8",
      "punkguitar": "emote-punkguitar",
      "raisetheroof": "emoji-celebrate",
      "russian": "dance-russian",
      "sad": "emote-sad",
      "savage": "dance-tiktok8",
      "shuffle": "dance-tiktok10",
      "shy": "emote-shy",
      "singalong": "idle_singing",
      "sit": "idle-loop-sitfloor",
      "snowangel": "emote-snowangel",
      "snowball": "emote-snowball",
      "swordfight": "emote-swordfight",
      "telekinesis": "emote-telekinesis",
      "teleport": "emote-teleporting",
      "thumbsup": "emoji-thumbsup",
      "tired": "emote-tired",
      "tummyache": "emoji-gagging",
      "viral": "dance-tiktok9",
      "wave": "emote-wave",
      "weird": "dance-weird",
      "worm": "emote-snake",
      "wrong": "dance-wrong",
      "yes": "emote-yes",
      "zombierun": "emote-zombierun",
      "ANGRY": "emoji-angry",
      "BOW": "emote-bow",
      "CASUAL": "idle-dance-casual",
      "CHARGING": "emote-charging",
      "CONFUSION": "emote-confused",
      "CURSING": "emoji-cursing",
      "CURTSY": "emote-curtsy",
      "CUTEY": "emote-cutey",
      "DONT": "dance-tiktok2",
      "EMOTECUTE": "emote-cute",
      "ENERGYBALL": "emote-energyball",
      "ENTHUSED": "idle-enthusiastic",
      "FASHIONISTA": "emote-fashionista",
      "FLEX": "emoji-flex",
      "FLIRTYWAVE": "emote-lust",
      "FLOAT": "emote-float",
      "FROG": "emote-frog",
      "GRAVEDANCE": "dance-weird",
      "GRAVITY": "emote-gravity",
      "GREEDY": "emote-greedy",
      "HELLO": "emote-hello",
      "HOT": "emote-hot",
      "ICECREAM": "dance-icecream",
      "KISS": "emote-kiss",
      "KPOP": "dance-blackpink",
      "LAMBI": "emote-superpose",
      "LAUGH": "emote-laughing",
      "LETSGO": "dance-shoppingcart",
      "MANIAC": "emote-maniac",
      "MODEL": "emote-model",
      "NO": "emote-no",
      "OGDANCE": "dance-macarena",
      "PENNYDANCE": "dance-pennywise",
      "POSE1": "emote-pose1",
      "POSE2": "emote-pose3",
      "POSE3": "emote-pose5",
      "POSE4": "emote-pose7",
      "POSE5": "emote-pose8",
      "PUNKGUITAR": "emote-punkguitar",
      "RAISETHEROOF": "emoji-celebrate",
      "RUSSIAN": "dance-russian",
      "SAD": "emote-sad",
      "SAVAGE": "dance-tiktok8",
      "SHUFFLE": "dance-tiktok10",
      "SHY": "emote-shy",
      "SINGALONG": "idle_singing",
      "SIT": "idle-loop-sitfloor",
      "SNOWANGEL": "emote-snowangel",
      "SNOWBALL": "emote-snowball",
      "SWORDFIGHT": "emote-swordfight",
      "TELEKINESIS": "emote-telekinesis",
      "TELEPORT": "emote-teleporting",
      "THUMBSUP": "emoji-thumbsup",
      "TIRED": "emote-tired",
      "TUMMYACHE": "emoji-gagging",
      "VIRAL": "dance-tiktok9",
      "WAVE": "emote-wave",
      "WEIRD": "dance-weird",
      "WORM": "emote-snake",
      "WRONG": "dance-wrong",
      "YES": "emote-yes",
      "ZOMBIERUN": "emote-zombierun",
      "1": "emoji-angry",
      "2": "emote-bow",
      "3": "idle-dance-casual",
      "4": "emote-charging",
      "5": "emote-confused",
      "5": "emoji-cursing",
      "6": "emote-curtsy",
      "7": "emote-cutey",
      "8": "dance-tiktok2",
      "9": "emote-cute",
      "10": "emote-energyball",
      "11": "idle-enthusiastic",
      "12": "emote-fashionista",
      "13": "emoji-flex",
      "14": "emote-lust",
      "15": "emote-float",
      "16": "emote-frog",
      "17": "dance-weird",
      "18": "emote-gravity",
      "19": "emote-greedy",
      "20": "emote-hello",
      "21": "emote-hot",
      "22": "dance-icecream",
      "23": "emote-kiss",
      "24": "dance-blackpink",
      "25": "emote-superpose",
      "26": "emote-laughing",
      "27": "dance-shoppingcart",
      "28": "emote-maniac",
      "29": "emote-model",
      "30": "emote-no",
      "31": "dance-macarena",
      "32": "dance-pennywise",
      "33": "emote-pose1",
      "34": "emote-pose3",
      "35": "emote-pose5",
      "36": "emote-pose7",
      "37": "emote-pose8",
      "38": "emote-punkguitar",
      "39": "emoji-celebrate",
      "40": "dance-russian",
      "41": "emote-sad",
      "42": "dance-tiktok8",
      "43": "dance-tiktok10",
      "44": "emote-shy",
      "45": "idle_singing",
      "46": "idle-loop-sitfloor",
      "47": "emote-snowangel",
      "48": "emote-snowball",
      "49": "emote-swordfight",
      "50": "emote-telekinesis",
      "51": "emote-teleporting",
      "52": "emoji-thumbsup",
      "53": "emote-tired",
      "54": "emoji-gagging",
      "55": "dance-tiktok9",
      "56": "emote-wave",
      "57": "dance-weird",
      "58": "emote-snake",
      "59": "dance-wrong",
      "60": "emote-yes",
      "61": "emote-zombierun",
      "62": "idle-dance-tiktok4",
      "63": "idle-uwu",
      "64": "emote-astronaut",
      "65": "emote-boxer",
      "66": "emote-pose9",
      "67": "emote-pose6",
      "68": "emote-celebrationstep",
      "69": "idle-guitar",
      "70": "dance-anime",
      "71": "dance-pinguin",
      "72": "dance-creepypuppet",
      "73": "emote-creepycute",
      "74": "dance-creepypuppet",
      "75": "emote-headblowup",
      "76": "emote-stargazer",
      "77": "emote-shy2",
      "78": "emote-celebrate",
      "79": "emote-iceskating",
      "80": "emote-timejump",
      "81": "idle-toilet",
      "82": "idle-wild",
      "83": "idle-nervous",
      "84": "emote-sleigh",
      "85": "dance-kawai",
      "86": "sit-relaxed",
      "87": "dance-employee",
      "88": "dance-touch",
      "89": "dance-tiktok11",
      "90": "emote-launch",
      "Angry": "emoji-angry",
      "Bow": "emote-bow",
      "Casual": "idle-dance-casual",
      "Charging": "emote-charging",
      "Confusion": "emote-confused",
      "Cursing": "emoji-cursing",
      "Curtsy": "emote-curtsy",
      "Cutey": "emote-cutey",
      "Dont": "dance-tiktok2",
      "Emotecute": "emote-cute",
      "Energyball": "emote-energyball",
      "Enthused": "idle-enthusiastic",
      "Fashionista": "emote-fashionista",
      "Flex": "emoji-flex",
      "Flirtywave": "emote-lust",
      "Float": "emote-float",
      "Frog": "emote-frog",
      "Gravedance": "dance-weird",
      "Gravity": "emote-gravity",
      "Greedy": "emote-greedy",
      "Hello": "emote-hello",
      "Hot": "emote-hot",
      "Icecream": "dance-icecream",
      "Kiss": "emote-kiss",
      "Kpop": "dance-blackpink",
      "Lambi": "emote-superpose",
      "Laugh": "emote-laughing",
      "Letsgo": "dance-shoppingcart",
      "Maniac": "emote-maniac",
      "Model": "emote-model",
      "No": "emote-no",
      "Ogdance": "dance-macarena",
      "Pennydance": "dance-pennywise",
      "Pose1": "emote-pose1",
      "Pose2": "emote-pose3",
      "Pose3": "emote-pose5",
      "Pose4": "emote-pose7",
      "Pose5": "emote-pose8",
      "Punkguitar": "emote-punkguitar",
      "Raisetheroof": "emoji-celebrate",
      "Russian": "dance-russian",
      "Sad": "emote-sad",
      "Savage": "dance-tiktok8",
      "Shuffle": "dance-tiktok10",
      "Shy": "emote-shy",
      "Singalong": "idle_singing",
      "Sit": "idle-loop-sitfloor",
      "Snowangel": "emote-snowangel",
      "Snowball": "emote-snowball",
      "Swordfight": "emote-swordfight",
      "Telekinesis": "emote-telekinesis",
      "Teleport": "emote-teleporting",
      "Thumbsup": "emoji-thumbsup",
      "Tired": "emote-tired",
      "Tummyache": "emoji-gagging",
      "Viral": "dance-tiktok9",
      "Wave": "emote-wave",
      "Weird": "dance-weird",
      "Worm": "emote-snake",
      "Wrong": "dance-wrong",
      "Yes": "emote-yes",
      "Zombierun": "emote-zombierun",
      "sayso": "idle-dance-tiktok4",
      "Sayso": "idle-dance-tiktok4",
      "SAYSO": "idle-dance-tiktok4",
      "uwu": "idle-uwu",
      "UWU": "idle-uwu",
      "Uwu": "idle-uwu",
      "zerogravity": "emote-astronaut",
      "Zerogravity": "emote-astronaut",
      "zero gravity": "emote-astronaut",
      "Zero gravity": "emote-astronaut",
      "boxer": "emote-boxer",
      "ditzy": "emote-pose9",
      "Boxer": "emote-boxer",
      "Ditzy": "emote-pose9",
      "surprise": "emote-pose6",
      "celebration": "emote-celebrationstep",
      "Surprise": "emote-pose6",
      "Celebration": "emote-celebrationstep",
      "airguitar": "idle-guitar",
      "Airguitar": "idle-guitar",
      "Saunter sway": "dance-anime",
      "saunter sway": "dance-anime",
      "Penguin": "dance-pinguin",
      "penguin": "dance-pinguin",
      "Creepy puppet": "dance-creepypuppet",
      "creepy puppet": "dance-creepypuppet",
      "Watch your back": "emote-creepycute",
      "Watch your back": "emote-creepycute",
      "Creepy puppet": "dance-creepypuppet",
      "creepy puppet": "dance-creepypuppet",
      "Revelations": "emote-headblowup",
      "revelations": "emote-headblowup",
      "Stargazing": "emote-stargazer",
      "stargazing": "emote-stargazer",
      "Star gazing": "emote-stargazer",
      "star gazing": "emote-stargazer",
      "Star": "emote-stargazer",
      "star": "emote-stargazer",
      "Bashful": "emote-shy2",
      "bashful": "emote-shy2",
      "Party time": "emote-celebrate",
      "party time": "emote-celebrate",
      "ice skating": "emote-iceskating",
      "Ice skating": "emote-iceskating",
      "Timejump": "emote-timejump",
      "timejump": "emote-timejump",
      "Time jump": "emote-timejump",
      "time jump": "emote-timejump",
      "Gotta go": "idle-toilet",
      "gotta go": "idle-toilet",
      "Scritchy": "idle-wild",
      "scritchy": "idle-wild",
      "bit nervous": "idle-nervous",
      "Bit nervous": "idle-nervous",
      "Jingle": "dance-jinglebell",
      "jingle": "dance-jinglebell",
      "Jingle bell": "dance-jinglebell",
      "jingle bell": "dance-jinglebell",
      "Sleigh ride": "emote-sleigh",
      "sleigh ride": "emote-sleigh",
      "kawai go go": "dance-kawai",
      "Kawai go go": "dance-kawai",
      "Repose": "sit-relaxed",
      "repose": "sit-relaxed",
      "pushit": "dance-employee",
      "Pushit": "dance-employee",
      "push it": "dance-employee",
      "Push it": "dance-employee",
      "Sweet little moves": "dance-touch",
      "sweet little moves": "dance-touch",
      "Wop dance": "dance-tiktok11",
      "wop dance": "dance-tiktok11",
      "launch": "emote-launch",
      "Launch": "emote-launch",
  }
  continuous_emote_task = None

  def __init__(self):
    super().__init__()
    self.joined_users = []  # List to store joined user data
    self.user_reactions = {}
    self.command_modules = {}
    self.user_positions = {}# A dictionary to store the loader
    self.spamming = False
    self.room_dictionary = {
        "room_1": "646dce94304425f9e19f5c48",
        "room_2": "64c56b3f93191a44cc2aaa53",
    }
    self.allowed_usernames = ["Dr_DeaTH", "iZexy", "__sohail"]
    self.load_developer_usernames()
    self.owner = ["Dr_DeaTH", "iZexy", "__sohail"]
    self.moderators = []
    self.invite_message = ''
    self.stop_signal = False
    self.AREA_MIN_X = 7.5
    self.AREA_MAX_X = 12.5
    self.AREA_MIN_Y = 5.0
    self.AREA_MAX_Y = 5.0
    self.AREA_MIN_Z = 0.5
    self.AREA_MAX_Z = 3.5

  OUTFITS = [[
      Item('clothing', 1, 'body-flesh', True, 26),
      Item('clothing', 1, 'eye-n_basic2018malesquaresleepy', False, 7),
      Item('clothing', 1, 'eyebrow-n_basic2018newbrows07', False, 7),
      Item('clothing', 1, 'nose-n_basic2018newnose05', False, 7),
      Item('clothing', 1, 'mouth-basic2018chippermouth', False, 7),
      Item('clothing', 1, 'watch-n_room32019blackwatch', False, 7),
      Item('clothing', 1, 'glasses-n_room12019circleshades', False, 7),
      Item('clothing', 1, 'earrings-n_room12019goldhoops', False, 7),
      Item('clothing', 1, 'hair_back-n_basic2018wavypulledback', False, 7),
      Item('clothing', 1, 'hair_front-n_malenew07', False, 7),
      Item('clothing', 1, 'shirt-n_2016fallblackkknottedtee', True, 7),
      Item('clothing', 1, 'pants-n_room32019highwasittrackshortsblack', False,
           7),
      Item('clothing', 1, 'shoes-n_room22019kneehighsblack', False, 7),
  ]]


  

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("BOT IN THE ROOM")  
    # Create tasks for all three loops
    send_continuous_emotes(self)
    quotes_loop_task = self.highrise.tg.create_task(self.quotes_loop())
    emote_loop_task = self.highrise.tg.create_task(self.emote_loop())

    # Teleport and start all three loops concurrently
    await asyncio.gather(
        self.highrise.teleport(session_metadata.user_id, Position(18.5, 0.0, 8.0, "FrontLeft")),
        quotes_loop_task,
        emote_loop_task
    )

    await asyncio.gather(quotes_loop_task, emote_loop_task)
   

  def load_developer_usernames(self):
    try:
        with open("mod.json", "r") as file:
            self.developer_usernames = json.load(file)
    except FileNotFoundError:
        pass

  def save_developer_usernames(self):
    with open("mod.json", "w") as file:
        json.dump(self.developer_usernames, file)

    async def on_message(self, user_id: str, conversation_id: str,
                         is_new_conversation: bool) -> None:
      response = await self.highrise.get_messages(conversation_id)
      message = ""

      if isinstance(response, GetMessagesRequest.GetMessagesResponse):
        if response.messages:
          message = response.messages[0].content
          print(message)

      if message:
        if message.lower() == "Hey" in message or "hey" in message or "hello" in message or "Hello" in message or "hi" in message or "Hi" in message or "hlo" in message or "Hlo" in message or "hola" in message or "Hola" in message:
          commands = ["Hey!", "Commands...", "list", "Emotelist"]
          for command in commands:
            await self.highrise.send_message(conversation_id, command)

        elif message.lower() == "join" in message or "Join" in message or "(join)" in message or "(Join)" in message or "( join )" in message or "( Join )" in message:
          commands = ["You Joined!", "Wait for the RESULT!"]
          for command in commands:
            await self.highrise.send_message(conversation_id, command)

        elif message.lower() == "List" in message or "list" in message or "!list" in message:
          command_list = [
              "Here is the list of commands...", "Emotelist", "Poeticrizz",
              "Rizz", "Joke", "Roastme", "Funfact", "Deathyear",
              "Lovepercentage", "Hatepercentage", "Iq"
          ]
          for command in command_list:
            await self.highrise.send_message(conversation_id, command)

        elif message.lower() == "mod commands" in message or "!mod" in message or "Mod" in message:
         await self.highrise.send_message(conversation_id,"\nHey, \nmod commands:\n1. ❤️ all (send heart to all)\n2. here @username (teleport nearby)\n3. scan @username (check stats)\n4. heart @username 1000 (send hearts)\nEnjoy!")

        elif message.lower() == "help" in message or "Help" in message or "!help" in message:
         await self.highrise.send_message(conversation_id,"\nHey,\ncommands:\n1. To repeat an emote, use 'Loop emote-emote' (e.g., 'Loop Sayso').\n2. Explore additional features by checking the bio or typing 'list'.\n3. Interested in your own bot? PM the owner for more info (Paid).\nEnjoy!")

        elif message.lower() == "Rent bot" in message or "Rent" in message or "!rent" in message or "rent bot" in message:
         await self.highrise.send_message(conversation_id,"\nHey\nGet a custom bot with 24/7 support & cool features! PM @iZexy for details. Only 5k/month.")

        elif message.lower() == "run inv" in message or "Run inv" in message:
          await self.highrise.send_message(conversation_id, "Invite sent Successfully!")
          await self.send_invite_to_all_conversations('65a2e7798facd682d7e6a5e4')

        elif message.lower() == "dm" in message or "Dm" in message:
          await self.highrise.send_message(conversation_id, "Giveaway Dm sent Successfully!")
          await self.follow_dm('65a2e7798facd682d7e6a5e4')

        elif message.lower() == "emotelist":
          await self.highrise.send_message(conversation_id, "emotelist...")
          await self.highrise.send_message(
              conversation_id,
              "angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\npennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun"
          )

        elif message == "you":
          await self.highrise.send_message(conversation_id, "👀")

        else:
          await self.highrise.send_message(conversation_id, "Hey how are you?")

  async def on_user_join(self, user: User,
                         position: Union[Position, AnchorPosition]) -> None:
    try:
      await self.highrise.send_whisper(
          user.id, f"Welcome @{user.username}\nType List or Check Bio‼️\nMessage Join in pm‼️ \nget a chance to win 1K GOLD")
      await self.tip_new_user(user, 1)
      await self.highrise.send_emote("emote-lust", user.id)
      await self.send_random_reactions(user.id, num_reactions=1, delay=1.55)
    except Exception as e:
      print("Error:", e)

  async def on_tip(self, sender: User, receiver: User,
                   tip: CurrencyItem | Item) -> None:
    print(
        f"{sender.username} tipped {receiver.username} an amount of {tip.amount}"
    )

  async def on_emote(self, user: User, emote_id: str,
                     receiver: User | None) -> None:
    print(f"{user.username} emoted: {emote_id}")

  async def on_whisper(self, user: User, message: str) -> None:
    print(f"{user.username} whispered: {message}")
    if user.username == "Dr_DeaTH" or user.username == "iZexy":
      await self.highrise.chat(message)

    if message.lstrip().startswith('og'):
      await self.send_invite_to_all_conversations('65a2e7798facd682d7e6a5e4')

    if message.lstrip().startswith('dm'):
      await self.follow_dm('65a2e7798facd682d7e6a5e4')
    
    if "Floor 1" in message.lower():
      try:
        await self.highrise.teleport(
            f"{user.id}", Position(7.0, 0.0, 16.0, facing='BackRight'))
      except Exception as e:
        print("error 3:", e)
    elif "333" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}", Position(11.5, 14.25, 9.5))
      except Exception as e:
        print("error 3:", e)
    elif "111" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}", Position(13.5, 6.0, 12.5))
      except Exception as e:
        print("error 3:", e)
    elif "offline" in message.lower():
      try:
        await self.highrise.teleport(f"{user.id}",
                                     Position(999.5, 999.75, 999.5))
      except Exception as e:
        print("error 3:", e)

  async def on_reaction(self, user: User, reaction: Reaction,
                        receiver: User) -> None:
    if user.username in moderators:
      if reaction == "wave":
       await self.highrise.moderate_room(receiver.id, "kick")
       await self.highrise.chat (f"\n@{receiver.username}❤️ \nHas been kicked")
    if receiver.username == "NamasteAgent":
      if reaction == "heart":
          await self.highrise.react("heart", user.id)
          await self.highrise.send_whisper(
            user.id, f"\nHow are you")
      if reaction == "wink":
        await self.highrise.react("wink", user.id)
      if reaction == "clap":
        await self.highrise.react("clap", user.id)
      if reaction == "thumbs":
        await self.highrise.react("thumbs", user.id)

      if reaction == "clap":
        bot_username = "NamasteAgent"  
        if user.username not in self.allowed_usernames:
            return

        room_users = (await self.highrise.get_room_users()).content

        for room_user, _ in room_users:
            if room_user.username != bot_username: 
                await self.highrise.react("clap", room_user.id)

      if reaction == "heart":
        bot_username = "NamasteAgent"  
        if user.username not in self.allowed_usernames:
            return

        room_users = (await self.highrise.get_room_users()).content

        for room_user, _ in room_users:
            if room_user.username != bot_username: 
                await self.highrise.react("heart", room_user.id)

      if reaction == "thumbs":
        bot_username = "NamasteAgent"  
        if user.username not in self.allowed_usernames:
            return

        room_users = (await self.highrise.get_room_users()).content

        for room_user, _ in room_users:
            if room_user.username != bot_username: 
                await self.highrise.react("thumbs", room_user.id)

      if reaction == "wink":
        bot_username = "NamasteAgent"  
        if user.username not in self.allowed_usernames:
            return

        room_users = (await self.highrise.get_room_users()).content

        for room_user, _ in room_users:
            if room_user.username != bot_username: 
                await self.highrise.react("wink", room_user.id)



      

 
              
  async def on_user_leave(self, user: User) -> None:
    print(f"{user.username} Left the Room")
    await self.stop_continuous_emote(user.id)

  async def on_chat(self, user: User, message: str) -> None:
    print(f"{user.username}:{message}")
    if message in self.EMOTE_DICT:
      emote_id = self.EMOTE_DICT[message]
      await self.highrise.send_emote(emote_id, user.id)
    

    if message.startswith("Loop"):
      emote_name = message[5:].strip()
      if emote_name in self.EMOTE_DICT:
        emote_id = self.EMOTE_DICT[emote_name]
        delay = 1
        if " " in emote_name:
          emote_name, delay_str = emote_name.split(" ")
          if delay_str.isdigit():
            delay = float(delay_str)

        if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
            user.id].cancelled():
          await self.stop_continuous_emote(user.id)

        task = asyncio.create_task(
            self.send_continuous_emote(emote_id, user.id, delay))
        self.continuous_emote_tasks[user.id] = task

    elif message.startswith("Stop"):
      if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
          user.id].cancelled():
        await self.stop_continuous_emote(user.id)

        await self.highrise.send_whisper(
          user.id, f"Continuous emote has been stopped.")
      else:
        await self.highrise.send_whisper(
          user.id, f"You don't have an active loop_emote.")

    elif message.lower().startswith("Bank"):
      wallet = (await self.highrise.get_wallet()).content
      await self.highrise.chat(
          f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")
    elif message.lower().startswith("Users"):
      room_users = (await self.highrise.get_room_users()).content
      await self.highrise.chat(f"There are {len(room_users)} users in the room"
                               )

    if message.lower().lstrip().startswith(
        ("anime", "fight", "penguin", "flirt", "stars", "gravity", "uwu",
         "zero", "fashion", "icecream", "punk", "wrong", "sayso", "zombie",
         "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance",
         "shuffle", "viral", "weird", "russian", "curtsy", "snowball",
         "sweating", "snowangel", "cute", "worm", "lambi", "celebration",
         "frog", "energyball", "maniac", "teleport", "float", "telekinesis",
         "enthused", "confused", "charging", "shopping", "bow", "savage",
         "kpop", "model", "dont", "pennywise", "flex", "gagging", "greedy",
         "cursing", "kiss")):
      response = await self.highrise.get_room_users()
      users = [content[0] for content in response.content]
      usernames = [user.username.lower() for user in users]
      parts = message[1:].split()
      args = parts[1:]

      if len(args) < 1:
        await self.highrise.send_whisper(user.id,
                                         f"Usage: {parts[0]} <@username>")
        return
      elif args[0][0] != "@":
        await self.highrise.send_whisper(
            user.id, "Invalid user format. Please use '@username'.")
        return
      elif args[0][1:].lower() not in usernames:
        await self.highrise.send_whisper(user.id,
                                         f"{args[0][1:]} is not in the room.")
        return

      user_id = next(
          (u.id for u in users if u.username.lower() == args[0][1:].lower()),
          None)
      if not user_id:
        await self.highrise.send_whisper(user.id,
                                         f"User {args[0][1:]} not found")
        return

      if message.lower().lstrip().startswith("fight"):
        await self.highrise.chat(f"\nLmao \n@{user.username} And @{args[0][1:]}\nBoxers...🌚")
        await self.highrise.send_emote("emote-boxer", user.id)
        await self.highrise.send_emote("emote-boxer", user_id)

      elif message.lower().lstrip().startswith("penguin"):
        await self.highrise.chat(f"\n🫂 @{user.username} And @{args[0][1:]} Both are penguins🐧❤️")
        await self.highrise.send_emote("dance-pinguin", user.id)
        await self.highrise.send_emote("dance-pinguin", user_id)

      elif message.lower().lstrip().startswith("flirt"):
        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} Flirting hmmm... 😏❤️")
        await self.highrise.send_emote("emote-lust", user.id)
        await self.highrise.send_emote("emote-lust", user_id)

      elif message.lower().lstrip().startswith("stars"):
        await self.highrise.send_emote("emote-stargazer", user.id)
        await self.highrise.send_emote("emote-stargazer", user_id)

      elif message.lower().lstrip().startswith("zero"):
        await self.highrise.send_emote("emote-astronaut", user.id)
        await self.highrise.send_emote("emote-astronaut", user_id)

      elif message.lower().lstrip().startswith("gravity"):
        await self.highrise.send_emote("emote-gravity", user.id)
        await self.highrise.send_emote("emote-gravity", user_id)

      elif message.lower().lstrip().startswith("uwu"):
        await self.highrise.send_emote("idle-uwu", user.id)
        await self.highrise.send_emote("idle-uwu", user_id)

      elif message.lower().lstrip().startswith("fashion"):
        await self.highrise.send_emote("emote-fashionista", user.id)
        await self.highrise.send_emote("emote-fashionista", user_id)

      elif message.lower().lstrip().startswith("icecream"):
        await self.highrise.send_emote("dance-icecream", user.id)
        await self.highrise.send_emote("dance-icecream", user_id)

      elif message.lower().lstrip().startswith("punk"):
        await self.highrise.send_emote("emote-punkguitar", user.id)
        await self.highrise.send_emote("emote-punkguitar", user_id)

      elif message.lower().lstrip().startswith("wrong"):
        await self.highrise.send_emote("dance-wrong", user.id)
        await self.highrise.send_emote("dance-wrong", user_id)

      elif message.lower().lstrip().startswith("sayso"):
        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

      elif message.lower().lstrip().startswith("zombie"):
        await self.highrise.send_emote("emote-zombierun", user.id)
        await self.highrise.send_emote("emote-zombierun", user_id)

      elif message.lower().lstrip().startswith("cutey"):
        await self.highrise.send_emote("emote-cutey", user.id)
        await self.highrise.send_emote("emote-cutey", user_id)

      elif message.lower().lstrip().startswith("anime"):
        await self.highrise.send_emote("dance-anime", user.id)
        await self.highrise.send_emote("dance-anime", user_id)

      elif message.lower().lstrip().startswith("pose3"):
        await self.highrise.send_emote("emote-pose3", user.id)
        await self.highrise.send_emote("emote-pose3", user_id)

      elif message.lower().lstrip().startswith("pose1"):
        await self.highrise.send_emote("emote-pose1", user.id)
        await self.highrise.send_emote("emote-pose1", user_id)

      elif message.lower().lstrip().startswith("pose7"):
        await self.highrise.send_emote("emote-pose7", user.id)
        await self.highrise.send_emote("emote-pose7", user_id)

      elif message.lower().lstrip().startswith("pose8"):
        await self.highrise.send_emote("emote-pose8", user.id)
        await self.highrise.send_emote("emote-pose8", user_id)

      elif message.lower().lstrip().startswith("dance"):
        await self.highrise.send_emote("idle-dance-casual", user.id)
        await self.highrise.send_emote("idle-dance-casual", user_id)

      elif message.lower().lstrip().startswith("shuffle"):
        await self.highrise.send_emote("dance-tiktok10", user.id)
        await self.highrise.send_emote("dance-tiktok10", user_id)

      elif message.lower().lstrip().startswith("weird"):
        await self.highrise.send_emote("emote-weird", user.id)
        await self.highrise.send_emote("emote-weird", user_id)

      elif message.lower().lstrip().startswith("viralgroove"):
        await self.highrise.send_emote("dance-tiktok9", user.id)
        await self.highrise.send_emote("dance-tiktok9", user_id)

      elif message.lower().lstrip().startswith("cute"):
        await self.highrise.send_emote("emote-cute", user.id)
        await self.highrise.send_emote("emote-cute", user_id)

      elif message.lower().lstrip().startswith("frog"):
        await self.highrise.send_emote("emote-frog", user.id)
        await self.highrise.send_emote("emote-frog", user_id)

      elif message.lower().lstrip().startswith("lambi"):
        await self.highrise.send_emote("emote-superpose", user.id)
        await self.highrise.send_emote("emote-superpose", user_id)

      elif message.lower().lstrip().startswith("celebration"):
        await self.highrise.send_emote("emote-celebrationstep", user.id)
        await self.highrise.send_emote("emote-celebrationstep", user_id)

      elif message.lower().lstrip().startswith("worm"):
        await self.highrise.send_emote("emote-snake", user.id)
        await self.highrise.send_emote("emote-snake", user_id)

      elif message.lower().lstrip().startswith("bow"):
        await self.highrise.send_emote("emote-bow", user.id)
        await self.highrise.send_emote("emote-bow", user_id)

      elif message.lower().lstrip().startswith("energyball"):
        await self.highrise.send_emote("emote-energyball", user.id)
        await self.highrise.send_emote("emote-energyball", user_id)

      elif message.lower().lstrip().startswith("maniac"):
        await self.highrise.send_emote("emote-maniac", user.id)
        await self.highrise.send_emote("emote-maniac", user_id)

      elif message.lower().lstrip().startswith("teleport"):
        await self.highrise.send_emote("emote-teleporting", user.id)
        await self.highrise.send_emote("emote-teleporting", user_id)

      elif message.lower().lstrip().startswith("float"):
        await self.highrise.send_emote("emote-float", user.id)
        await self.highrise.send_emote("emote-float", user_id)

      elif message.lower().lstrip().startswith("telekinesis"):
        await self.highrise.send_emote("emote-telekinesis", user.id)
        await self.highrise.send_emote("emote-telekinesis", user_id)

      elif message.lower().lstrip().startswith("enthused"):
        await self.highrise.send_emote("idle-enthusiastic", user.id)
        await self.highrise.send_emote("idle-enthusiastic", user_id)

      elif message.lower().lstrip().startswith("confused"):
        await self.highrise.send_emote("emote-confused", user.id)
        await self.highrise.send_emote("emote-confused", user_id)

      elif message.lower().lstrip().startswith("shopping"):
        await self.highrise.send_emote("dance-shoppingcart", user.id)
        await self.highrise.send_emote("dance-shoppingcart", user_id)

      elif message.lower().lstrip().startswith("charging"):
        await self.highrise.send_emote("emote-charging", user.id)
        await self.highrise.send_emote("emote-charging", user_id)

      elif message.lower().lstrip().startswith("snowangel"):
        await self.highrise.send_emote("emote-snowangel", user.id)
        await self.highrise.send_emote("emote-snowangel", user_id)

      elif message.lower().lstrip().startswith("sweating"):
        await self.highrise.send_emote("emote-hot", user.id)
        await self.highrise.send_emote("emote-hot", user_id)

      elif message.lower().lstrip().startswith("snowball"):
        await self.highrise.send_emote("emote-snowball", user.id)
        await self.highrise.send_emote("emote-snowball", user_id)

      elif message.lower().lstrip().startswith("curtsy"):
        await self.highrise.send_emote("emote-curtsy", user.id)
        await self.highrise.send_emote("emote-curtsy", user_id)

      elif message.lower().lstrip().startswith("russian"):
        await self.highrise.send_emote("dance-russian", user.id)
        await self.highrise.send_emote("dance-russian", user_id)

      elif message.lower().lstrip().startswith("pennywise"):
        await self.highrise.send_emote("dance-pennywise", user.id)
        await self.highrise.send_emote("dance-pennywise", user_id)

      elif message.lower().lstrip().startswith("dont"):
        await self.highrise.send_emote("dance-tiktok2", user.id)
        await self.highrise.send_emote("dance-tiktok2", user_id)

      elif message.lower().lstrip().startswith("kpop"):
        await self.highrise.send_emote("dance-blackpink", user.id)
        await self.highrise.send_emote("dance-blackpink", user_id)

      elif message.lower().lstrip().startswith("model"):
        await self.highrise.send_emote("emote-model", user.id)
        await self.highrise.send_emote("emote-model", user_id)

      elif message.lower().lstrip().startswith("savage"):
        await self.highrise.send_emote("dance-tiktok8", user.id)
        await self.highrise.send_emote("dance-tiktok8", user_id)

      elif message.lower().lstrip().startswith("flex"):
        await self.highrise.send_emote("emoji-flex", user.id)
        await self.highrise.send_emote("emoji-flex", user_id)

      elif message.lower().lstrip().startswith("gagging"):
        await self.highrise.send_emote("emoji-gagging", user.id)
        await self.highrise.send_emote("emoji-gagging", user_id)

      elif message.lower().lstrip().startswith("greedy"):
        await self.highrise.send_emote("emote-greedy", user.id)
        await self.highrise.send_emote("emote-greedy", user_id)

      elif message.lower().lstrip().startswith("cursing"):
        await self.highrise.send_emote("emoji-cursing", user.id)
        await self.highrise.send_emote("emoji-cursing", user_id)

      elif message.lower().lstrip().startswith("zero"):
        await self.highrise.send_emote("emote-astronaut", user.id)
        await self.highrise.send_emote("emote-astronaut", user_id)

      elif message.lower().lstrip().startswith("kiss"):
        await self.highrise.send_emote("emote-kiss", user.id)
        await self.highrise.send_emote("eote-kiss", user_id)

  #TO_BUY ROOM boost

    if message.lower().startswith(
        "b00st") and user.username in self.allowed_usernames:
      response = await self.highrise.buy_room_boost(payment="bot_wallet_only",
                                                  amount=1)
      print(response)
      await self.highrise.send_whisper(user.id, f"The bot have:\n{response}")

    try:
      if message.startswith("here") or message.startswith("Here"):
          if user.username in self.developer_usernames:
              target_username = message.split("@")[-1].strip()
              if target_username not in self.moderators:
                  await self.teleport_user_next_to(target_username, user)
    except Exception as e:
      print(f"An error occurred: {str(e)}")



    if message == "tip1" and user.username in self.allowed_usernames:
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          await self.highrise.tip_user(roomUser.id, "gold_bar_1")


    if message.startswith("❤️ all"):
      bot_username = "NamasteAgent"  
      if user.username not in self.developer_usernames:
          await self.highrise.send_whisper(user.id, "Done!")
          return

      room_users = (await self.highrise.get_room_users()).content

      for room_user, _ in room_users:
          if room_user.username != bot_username: 
              await self.highrise.react("heart", room_user.id)

    if message.startswith("👍 all"):
      bot_username = "NamasteAgent"  
      if user.username not in self.developer_usernames:
          await self.highrise.send_whisper(user.id, "Done!")
          return

      room_users = (await self.highrise.get_room_users()).content

      for room_user, _ in room_users:
          if room_user.username != bot_username: 
              await self.highrise.react("thumbs", room_user.id)

    if message.startswith("👏 all"):
      bot_username = "NamasteAgent"  
      if user.username not in self.developer_usernames:
          await self.highrise.send_whisper(user.id, "Done!")
          return

      room_users = (await self.highrise.get_room_users()).content

      for room_user, _ in room_users:
          if room_user.username != bot_username: 
              await self.highrise.react("clap", room_user.id)

    if message.startswith("😉 all"):
      bot_username = "NamasteAgent"  
      if user.username not in self.developer_usernames:
          await self.highrise.send_whisper(user.id, "Done!")
          return

      room_users = (await self.highrise.get_room_users()).content

      for room_user, _ in room_users:
          if room_user.username != bot_username: 
              await self.highrise.react("wink", room_user.id)

    if message == "Round":
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))

    if message == "Fly high":
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 1.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 3.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 4.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 5.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 6.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 7.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 8.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 9.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 10.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 11.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 12.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 13.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 14.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 15.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 16.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 17.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 18.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 19.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 20.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 21.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 22.0, 21.5)) 
     await self.highrise.teleport(user.id, Position(5.5, 23.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 24.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 25.0, 21.5))
     await self.highrise.teleport(user.id, Position(5.5, 2.0, 21.5))


     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
     await self.highrise.teleport(user.id, Position(17.5, 0.0, 19.5))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0)) 
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 10.0))
     await self.highrise.teleport(user.id, Position(0.5, 0.0, 2.5))
     await self.highrise.teleport(user.id, Position(1.0, 0.0, 19.0))
     await self.highrise.teleport(user.id, Position(10.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 4.0))
     await self.highrise.teleport(user.id, Position(18.0, 0.0, 9.5))
      
    if message.lower().startswith("!draw") and user.username in self.allowed_usernames:
      room_users = await self.highrise.get_room_users()

      if room_users and room_users.content:
          random_user = random.choice(room_users.content)
          selected_user = random_user[0]

          await self.highrise.chat(f"The selected user is: @{selected_user.username}")
      else:
          await self.highrise.chat("There are no users in the room to draw from!")

    if message.lower().startswith("!chemistry"):
      # Extract the target user's name from the message
      target_user = message.split("chemistry", 1)[-1].strip()
      # Generate a fictional chemistry probability between 0% and 100%
      chemistry_probability = random.randint(0, 100)
      # Create a response message with the chemistry probability
      response = f"your chemistry with {target_user} is {chemistry_probability}%"
      # Send the response in Highrise style
      await self.highrise.chat(response)

    if message.lower().startswith("!love"):
      # Extract the target user's name from the message
      target_user = message.split("love", 1)[-1].strip()
      # Generate a fictional chemistry probability between 0% and 100%
      chemistry_probability = random.randint(0, 100)
      # Create a response message with the chemistry probability
      response = f"your love for {target_user} is {chemistry_probability}%"
      # Send the response in Highrise style
      await self.highrise.chat(response)

    if message.lower().startswith("!hate"):
      # Extract the target user's name from the message
      target_user = message.split("hate", 1)[-1].strip()
      # Generate a fictional chemistry probability between 0% and 100%
      chemistry_probability = random.randint(0, 100)
      # Create a response message with the chemistry probability
      response = f"your hate for {target_user} is {chemistry_probability}%"
      # Send the response in Highrise style
      await self.highrise.chat(response)

    if message.lower().startswith("!interest"):
      # Extract the target user's name from the message
      target_user = message.split("interest", 1)[-1].strip()
      # Generate a fictional chemistry probability between 0% and 100%
      chemistry_probability = random.randint(0, 100)
      # Create a response message with the chemistry probability
      response = f"your interest for {target_user} is {chemistry_probability}%"
      # Send the response in Highrise style
      await self.highrise.chat(response)

    if message.lower().startswith("/g ") and user.username in self.allowed_usernames:
      parts = message.split(" ")
      if len(parts) != 2:
        await self.highrise.send_whisper(user.id, f"Invalid command")
        return
      try:
        amount = int(parts[1])
      except:
        await self.highrise.chat("Invalid amount")
      bot_wallet = await self.highrise.get_wallet()
      bot_amount = bot_wallet.content[0].amount
      if bot_amount <= amount:
        await self.highrise.chat("I don't have Hehe")
        return
      bars_dictionary = {
          10000: "gold_bar_10k",
          5000: "gold_bar_5000",
          1000: "gold_bar_1k",
          500: "gold_bar_500",
          100: "gold_bar_100",
          50: "gold_bar_50",
          10: "gold_bar_10",
          5: "gold_bar_5",
          1: "gold_bar_1"
      }
      fees_dictionary = {
          10000: 1000,
          5000: 500,
          1000: 100,
          500: 50,
          100: 10,
          50: 5,
          10: 1,
          5: 1,
          1: 1
      }
      tip = []
      total = 0
      for bar in bars_dictionary:
        if amount >= bar:
          bar_amount = amount // bar
          amount = amount % bar
          for i in range(bar_amount):
            tip.append(bars_dictionary[bar])
            total = bar + fees_dictionary[bar]
      if total > bot_amount:
        await self.highrise.send_whisper(user.id, f"i don't have hehe")
        return
      for bar in tip:
        await self.highrise.tip_user(user.id, bar)

    if message.startswith("!mod @") and user.username in self.owner:
      username = message.split("@")[1].strip()
      if username not in self.developer_usernames:
          self.developer_usernames.append(username)
          self.save_developer_usernames()
          print("Developer user list updated:", self.developer_usernames)
      else:
          print(f"{username} is already in the developer list.")
    elif message.startswith("!remove @") and user.username in self.owner:
      username = message.split("@")[1].strip()
      if username in self.developer_usernames:
          self.developer_usernames.remove(username)
          self.save_developer_usernames()
          print("Developer user removed:", username)
      else:
          print(f"{username} is not in the developer list.")

    if message.lower().startswith("heart ") and user.username in self.developer_usernames:
      try:
        # استخراج العدد المطلوب واسم المستخدم من الرسالة
        parts = message.split()
        num_hearts = int(parts[-1])
        target_username = parts[1].strip('@').lower()

        if 1 <= num_hearts <= 1000:
          for _ in range(num_hearts):
            target_user = None
            response = await self.highrise.get_room_users()
            for user_info in response.content:
              if user_info[0].username.lower() == target_username:
                target_user = user_info[0]
                break

            if target_user:
              await self.highrise.react("heart", target_user.id)

        else:

          await self.highrise.chat("1  _ 100  only ")
      except ValueError:
        await self.highrise.chat("heart @user")

    if message.lower().startswith("wink ") and user.username in self.developer_usernames:
      try:
        # استخراج العدد المطلوب واسم المستخدم من الرسالة
        parts = message.split()
        num_hearts = int(parts[-1])
        target_username = parts[1].strip('@').lower()

        if 1 <= num_hearts <= 1000:
          for _ in range(num_hearts):
            target_user = None
            response = await self.highrise.get_room_users()
            for user_info in response.content:
              if user_info[0].username.lower() == target_username:
                target_user = user_info[0]
                break

            if target_user:
              await self.highrise.react("wink", target_user.id)

        else:

          await self.highrise.chat("1  _ 100  only ")
      except ValueError:
        await self.highrise.chat("wink @user")

    if message.lower().startswith("thumbs ") and user.username in self.developer_usernames:
      try:
        # استخراج العدد المطلوب واسم المستخدم من الرسالة
        parts = message.split()
        num_hearts = int(parts[-1])
        target_username = parts[1].strip('@').lower()

        if 1 <= num_hearts <= 1000:
          for _ in range(num_hearts):
            target_user = None
            response = await self.highrise.get_room_users()
            for user_info in response.content:
              if user_info[0].username.lower() == target_username:
                target_user = user_info[0]
                break

            if target_user:
              await self.highrise.react("thumbs", target_user.id)

        else:

          await self.highrise.chat("1  _ 100  only ")
      except ValueError:
        await self.highrise.chat("thumbs @user")

    if message.lower().startswith("auto dance") or \
     message.lower().startswith("!auto dance") or \
     message.lower().startswith("Auto dance") or \
     message.lower().startswith("!Auto dance"):
      await self.dance_sequence(user)


    if message.lower() == "stop":
      self.stop_signal = True
      await self.highrise.send_whisper(user.id, "Stopped the dance.")
    elif message.lower() in ["auto dance", "!auto dance"]:
      self.stop_signal = False  # Reset stop signal before starting the dance
      await self.dance_sequence(user)

    if message.lower().startswith("clap ") and user.username in self.developer_usernames:
      try:
        # استخراج العدد المطلوب واسم المستخدم من الرسالة
        parts = message.split()
        num_hearts = int(parts[-1])
        target_username = parts[1].strip('@').lower()

        if 1 <= num_hearts <= 1000:
          for _ in range(num_hearts):
            target_user = None
            response = await self.highrise.get_room_users()
            for user_info in response.content:
              if user_info[0].username.lower() == target_username:
                target_user = user_info[0]
                break

            if target_user:
              await self.highrise.react("clap", target_user.id)

        else:

          await self.highrise.chat("1  _ 100  only ")
      except ValueError:
        await self.highrise.chat("clap @user")

    if message.lower().startswith("!"):
      country_name = message.split("!")[1].strip()  # Extract the country name from the message
      country_info = get_country_info(country_name)

      if country_info:
          response_message = (
              f"Country: {country_info['name']}\n"
              f"Population: {country_info['population']}\n"
              f"Currencies: {', '.join(country_info['currencies'])}\n"
              f"Languages: {', '.join(country_info['languages'])}"
          )


    emote_mapping = {
        "/charging": "emote-charging",
        "/energyball": "emote-energyball",
        "/fashionista": "emote-fashionista",
        "/flex": "emoji-flex",
        "/flirtywave": "emote-lust",
        "/float": "emote-float",
        "/frog": "emote-frog",
        "/gravedance": "dance-weird",
        "/gravity": "emote-gravity",
        "/greedy": "emote-greedy",
        "/hello": "emote-hello",
        "/hot": "emote-hot",
        "/icecream": "dance-icecream",
        "/kiss": "emote-kiss",
        "/kpop": "dance-blackpink",
        "/lambi": "emote-superpose",
        "/laugh": "emote-laughing",
        "/letsgo": "dance-shoppingcart",
        "/maniac": "emote-maniac",
        "/model": "emote-model",
        "/no": "emote-no",
        "/ogdance": "dance-macarena",
        "/pennydance": "dance-pennywise",
        "/pose1": "emote-pose1",
        "/pose2": "emote-pose3",
        "/pose3": "emote-pose5",
        "/pose4": "emote-pose7",
        "/pose5": "emote-pose8",
        "/punkguitar": "emote-punkguitar",
        "/raisetheroof": "emoji-celebrate",
        "/russian": "dance-russian",
        "/sad": "emote-sad",
        "/savage": "dance-tiktok8",
        "/shuffle": "dance-tiktok10",
        "/shy": "emote-shy",
        "/singalong": "idle_singing",
        "/sit": "idle-loop-sitfloor",
        "/snowangel": "emote-snowangel",
        "/snowball": "emote-snowball",
        "/swordfight": "emote-swordfight",
        "/telekinesis": "emote-telekinesis",
        "/teleport": "emote-teleporting",
        "/thumbsup": "emoji-thumbsup",
        "/tired": "emote-tired",
        "/tummyache": "emoji-gagging",
        "/viral": "dance-tiktok9",
        "/wave": "emote-wave",
        "/weird": "dance-weird",
        "/worm": "emote-snake",
        "/wrong": "dance-wrong",
        "/yes": "emote-yes",
        "/zombierun": "emote-zombierun",
        "/ANGRY": "emoji-angry",
        "/BOW": "emote-bow",
        "/CASUAL": "idle-dance-casual",
        "/CHARGING": "emote-charging",
        "/CONFUSION": "emote-confused",
        "/CURSING": "emoji-cursing",
        "/CURTSY": "emote-curtsy",
        "/CUTEY": "emote-cutey",
        "/DONT": "dance-tiktok2",
        "/EMOTECUTE": "emote-cute",
        "/ENERGYBALL": "emote-energyball",
        "/ENTHUSED": "idle-enthusiastic",
        "/FASHIONISTA": "emote-fashionista",
        "/FLEX": "emoji-flex",
        "/FLIRTYWAVE": "emote-lust",
        "/FLOAT": "emote-float",
        "/FROG": "emote-frog",
        "/GRAVEDANCE": "dance-weird",
        "/GRAVITY": "emote-gravity",
        "/GREEDY": "emote-greedy",
        "/HELLO": "emote-hello",
        "/HOT": "emote-hot",
        "/ICECREAM": "dance-icecream",
        "/KISS": "emote-kiss",
        "/KPOP": "dance-blackpink",
        "/LAMBI": "emote-superpose",
        "/LAUGH": "emote-laughing",
        "/LETSGO": "dance-shoppingcart",
        "/MANIAC": "emote-maniac",
        "/MODEL": "emote-model",
        "/NO": "emote-no",
        "/OGDANCE": "dance-macarena",
        "/PENNYDANCE": "dance-pennywise",
        "/POSE1": "emote-pose1",
        "/POSE2": "emote-pose3",
        "/POSE3": "emote-pose5",
        "/POSE4": "emote-pose7",
        "/POSE5": "emote-pose8",
        "/PUNKGUITAR": "emote-punkguitar",
        "/RAISETHEROOF": "emoji-celebrate",
        "/RUSSIAN": "dance-russian",
        "/SAD": "emote-sad",
        "/SAVAGE": "dance-tiktok8",
        "/SHUFFLE": "dance-tiktok10",
        "/SHY": "emote-shy",
        "/SINGALONG": "idle_singing",
        "/SIT": "idle-loop-sitfloor",
        "/SNOWANGEL": "emote-snowangel",
        "/SNOWBALL": "emote-snowball",
        "/SWORDFIGHT": "emote-swordfight",
        "/TELEKINESIS": "emote-telekinesis",
        "/TELEPORT": "emote-teleporting",
        "/THUMBSUP": "emoji-thumbsup",
        "/TIRED": "emote-tired",
        "/TUMMYACHE": "emoji-gagging",
        "/VIRAL": "dance-tiktok9",
        "/WAVE": "emote-wave",
        "/WEIRD": "dance-weird",
        "/WORM": "emote-snake",
        "/WRONG": "dance-wrong",
        "/YES": "emote-yes",
        "/ZOMBIERUN": "emote-zombierun",
        "/Angry": "emoji-angry",
        "/Bow": "emote-bow",
        "/Casual": "idle-dance-casual",
        "/Charging": "emote-charging",
        "/Confusion": "emote-confused",
        "/Cursing": "emoji-cursing",
        "/Curtsy": "emote-curtsy",
        "/Cutey": "emote-cutey",
        "/Dont": "dance-tiktok2",
        "/Emotecute": "emote-cute",
        "/Energyball": "emote-energyball",
        "/Enthused": "idle-enthusiastic",
        "/Fashionista": "emote-fashionista",
        "/Flex": "emoji-flex",
        "/Flirtywave": "emote-lust",
        "/Float": "emote-float",
        "/Frog": "emote-frog",
        "/Gravedance": "dance-weird",
        "/Gravity": "emote-gravity",
        "/Greedy": "emote-greedy",
        "/Hello": "emote-hello",
        "/Hot": "emote-hot",
        "/Icecream": "dance-icecream",
        "/Kiss": "emote-kiss",
        "/Kpop": "dance-blackpink",
        "/Lambi": "emote-superpose",
        "/Laugh": "emote-laughing",
        "/Letsgo": "dance-shoppingcart",
        "/Maniac": "emote-maniac",
        "/Model": "emote-model",
        "/No": "emote-no",
        "/Ogdance": "dance-macarena",
        "/Pennydance": "dance-pennywise",
        "/Pose1": "emote-pose1",
        "/Pose2": "emote-pose3",
        "/Pose3": "emote-pose5",
        "/Pose4": "emote-pose7",
        "/Pose5": "emote-pose8",
        "/Punkguitar": "emote-punkguitar",
        "/Raisetheroof": "emoji-celebrate",
        "/Russian": "dance-russian",
        "/Sad": "emote-sad",
        "/Savage": "dance-tiktok8",
        "/Shuffle": "dance-tiktok10",
        "/Shy": "emote-shy",
        "/Singalong": "idle_singing",
        "/Sit": "idle-loop-sitfloor",
        "/Snowangel": "emote-snowangel",
        "/Snowball": "emote-snowball",
        "/Swordfight": "emote-swordfight",
        "/Telekinesis": "emote-telekinesis",
        "/Teleport": "emote-teleporting",
        "/Thumbsup": "emoji-thumbsup",
        "/Tired": "emote-tired",
        "/Tummyache": "emoji-gagging",
        "/Viral": "dance-tiktok9",
        "/Wave": "emote-wave",
        "/Weird": "dance-weird",
        "/Worm": "emote-snake",
        "/Wrong": "dance-wrong",
        "/Yes": "emote-yes",
        "/Zombierun": "emote-zombierun",
        "/sayso": "idle-dance-tiktok4",
        "/Sayso": "idle-dance-tiktok4",
        "/SAYSO": "idle-dance-tiktok4",
        "/uwu": "idle-uwu",
        "/UWU": "idle-uwu",
        "/Uwu": "idle-uwu",
        "/zerogravity": "emote-astronaut",
        "/Zerogravity": "emote-astronaut",
        "/zero gravity": "emote-astronaut",
        "/Zero gravity": "emote-astronaut",
        "/boxer": "emote-boxer",
        "/ditzy": "emote-pose9",
        "/Boxer": "emote-boxer",
        "/Ditzy": "emote-pose9",
        "/surprise": "emote-pose6",
        "/celebration": "emote-celebrationstep",
        "/Surprise": "emote-pose6",
        "/Celebration": "emote-celebrationstep",
        "/airguitar": "idle-guitar",
        "/Airguitar": "idle-guitar",
        "/Saunter sway": "dance-anime",
        "/saunter sway": "dance-anime",
        "/Penguin": "dance-pinguin",
        "/penguin": "dance-pinguin",
        "/Creepy puppet": "dance-creepypuppet",
        "/creepy puppet": "dance-creepypuppet",
        "/Watch your back": "emote-creepycute",
        "/watch your back": "emote-creepycute",
        "/Creepy puppet": "dance-creepypuppet",
        "/creepy puppet": "dance-creepypuppet",
        "/Revelations": "emote-headblowup",
        "/revelations": "emote-headblowup",
        "/Stargazing": "emote-stargazer",
        "/stargazing": "emote-stargazer",
        "/Star gazing": "emote-stargazer",
        "/star gazing": "emote-stargazer",
        "/Star": "emote-stargazer",
        "/star": "emote-stargazer",
        "/Bashful": "emote-shy2",
        "/bashful": "emote-shy2",
        "/Party time": "emote-celebrate",
        "/party time": "emote-celebrate",
        "/ice skating": "emote-iceskating",
        "/Ice skating": "emote-iceskating",
        "/Timejump": "emote-timejump",
        "/timejump": "emote-timejump",
        "/Time jump": "emote-timejump",
        "/time jump": "emote-timejump",
        "/Gotta go": "idle-toilet",
        "/gotta go": "idle-toilet",
        "/Scritchy": "idle-wild",
        "/scritchy": "idle-wild",
        "/bit nervous": "idle-nervous",
        "/Bit nervous": "idle-nervous",
        "/Jingle": "dance-jinglebell",
        "/jingle": "dance-jinglebell",
        "/Jingle bell": "dance-jinglebell",
        "/jingle bell": "dance-jinglebell",
        "/Sleigh ride": "emote-sleigh",
        "/sleigh ride": "emote-sleigh",
        "/kawai go go": "dance-kawai",
        "/Kawai go go": "dance-kawai",
        "/Repose": "sit-relaxed",
        "/repose": "sit-relaxed",
        "/pushit": "dance-employee",
        "/Pushit": "dance-employee",
        "/push it": "dance-employee",
        "/Push it": "dance-employee",
        "/Sweet little moves": "dance-touch",
        "/sweet little moves": "dance-touch",
        "/Wop dance": "dance-tiktok11",
        "/wop dance": "dance-tiktok11",
        "/launch": "emote-launch",
        "/Launch": "emote-launch",
    }

    # تحقق من البداية وقم بإرسال الرقصة المناسبة لجميع المستخدمين في الغرفة
    for key, emote in emote_mapping.items():
      if message.startswith(key) and user.username in self.allowed_usernames:
        roomUsers = (await self.highrise.get_room_users()).content
        for roomUser, _ in roomUsers:
          if isinstance(roomUser, User):
            await self.highrise.send_emote(emote, roomUser.id)
          else:
            print("Ignoring non-User object in roomUsers")
        break  # لا حاجة للاستمرار بعد العثور على النطاق المناس

     

    if "Floor 1" in message or "floor 1" in message or "!floor 1" in message or "!Floor 1" in message:
      await self.highrise.teleport(f"{user.id}", Position(15.5, 0.25, 8.5))

    if "Floor 2" in message or "floor 2" in message or "!floor 2" in message or "!Floor 2" in message:
      await self.highrise.teleport(f"{user.id}", Position(12.5, 8.75, 11.5))

    if "Floor 3" in message or "floor 3" in message or "!floor 3" in message or "!Floor 3" in message:
      await self.highrise.teleport(f"{user.id}", Position(12.5, 16.5, 12.5))

    if "Floor 4" in message or "floor 4" in message or "!floor 4" in message or "!Floor 4" in message:
      await self.highrise.teleport(f"{user.id}", Position(14.5, 23.0, 3.5))

    if "Oyo" in message or "oyo" in message or "!oyo" in message or "!Oyo" in message:
      await self.highrise.teleport(f"{user.id}", Position(11.5, 0.0, 1.0))

    if "Dancefloor" in message or "dancefloor" in message or "!dancefloor" in message or "!Dancefloor" in message:
      await self.highrise.teleport(f"{user.id}", Position(9.5, 5.0, 2.5))

    if "List" in message or "list" in message or "!list" in message:
      await self.highrise.send_whisper(user.id, "Commands‼️\nEmotes\nLoop (emote-name)\nEmotelist\nLovepercentage\nHatepercentage\nIq\nRoast\nRizz\nPoeticrizz\nJokes\nFunfact")
      await self.highrise.send_whisper(user.id, "more soon...")

    if "help" in message or "Help" in message or "!help" in message:
      await self.highrise.send_whisper(user.id,"\nHey,\ncommands:\n1. To repeat an emote, use 'Loop emote-emote' (e.g., 'Loop Sayso').\n2. Explore additional features by checking the bio or typing 'list'.\n3. Interested in your own bot? PM the owner for more info (Paid).\nEnjoy!")

    if "mod commands" in message or "!mod" in message or "Mod" in message:
      await self.highrise.send_whisper(user.id,"\nHey, \nmod commands:\n1. ❤️ all (send heart to all)\n2. here @username (teleport nearby)\n3. scan @username (check stats)\n4. heart @username 1000 (send hearts)\nEnjoy!")

    if "Rent bot" in message or "Rent" in message or "!rent" in message or "rent bot" in message:
      await self.highrise.chat(f"\nHey {user.username},\nGet a custom bot with 24/7 support & cool features! PM the room owner for details. Only 5k/month.")


    if "Hru" in message or "How are you" in message or "how are you" in message:
      await self.highrise.send_whisper(user.id,"\nThank you for asking! As a computer program, I don't have feelings, but I'm here and ready to assist you.")

    if "Emotelist" in message or "emotes" in message or "Emotes" in message or "!emotelist" in message:
      await self.highrise.send_whisper(
          user.id,
          "angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\n"
      )
      await self.highrise.send_whisper(
          user.id,
          "pennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun"
      )
      await self.highrise.send_whisper(
          user.id,
          "\nBoxer\nDitzy\nSurprise\nCelebration\nAirguitar\nPenguin\nWatch your back\nRevelations\nCreppy puppet\nStar gazer\nsaunter sway\nMore emotes Soon..."
      )

    if "Poeticrizz" in message or "poeticrizz" in message:
      poeticrizz = random.choice([
          "If you carried medusa’s curse, i would stare into your eyes so that my stone would gaze at your beauty for all eternity.",
          "If every star were a memory, i’d spend an eternity counting them all, just to relieve the moments I’ve spent with you",
          "As the sun comes up, you have no shadow, because there’s nothing that can replicate your beauty",
          "When i can’t be with you, i read your favorite book, listen to your favorite song, watch your favorite movie, because in them i find little bits of you",
          "My darkest days are shifted with a slight gaze of your fascinating looks. Your beautiful dark eyes are the last fiber holding my shattered heart.",
          "If I could weave a tapestry of our love, it would be a kaleidoscope of colors, each hue a testament to the depth of our affection.",
          "Your presence is like a sunrise, a radiant glow that banishes the darkness and fills my world with light.",
          "If I could sail the seas of time, I’d chart a course to the moment we first met, the instant our hearts became entwined.",
          "Your love is the anchor that holds me steady, a steadfast bond that keeps me grounded and secure.",
          "If I could gather the sands of the desert, I’d create a monument to your beauty, a testament to your enchanting allure.",
          "Your voice is the siren’s call, a mesmerizing melody that lures me into the depths of your love.",
          "If you’re the moon, i am the tide, for i flow under your command, forever longing for you, as you are my purpose.",
          "If i had to wait my entire life for your love, I would. For when i have withered away, i’d be glad i got to experience heaven before i reached it.",
          "For every star in the sky that went out, i would never know for you outshined them always.",
          "If you were a grain of sand, I’d search every beach and desert looking for you and your beauty no matter how long i’d have to look. ",
          "If you’re the angel of death, I’d be willing to die a million times just to see your beauty.",
          "If i was blinded the moment i lay my eyes on you, I would not grieve, for in that instance, i truly gazed upon perfection. ",
          "You are the sun to my sunflower, i will always be glancing at your gorgeous light as i follow you around amidst the bright morning.",
          "If i were dared to shout to the world how much i love you, i would simply whisper it in your ears.",
          "Your love is the beacon that guides me through the darkest storms, a lighthouse illuminating my heart’s shore.",
          "If your heart were a canvas, I’d paint it with the colors of a thousand sunsets, each hue a testament to my love for you. ",
          "Like a rose in full bloom, your beauty captivates me, leaving me breathless and longing for your tender embrace. ",
          "If i had to wait my entire life for your love, i would. When i’ve withered away, I’d be glad i got to experience heaven before i reached it.",
          "If i had a flower for every time i thought of you, I’d have one, because not once have i stopped thinking about the perfection that you are.",
          "If I could rearrange the cosmos, I would replace the sun with you for your beauty shines brighter than any star ever will my dear",
          "The stars were so jealous of how bright you were, they had to make the sun fall just to be seen, yet you outshined them everytime.",
          "Even if i learned every language, i couldn’t find the words to describe how beautiful you are.",
          "Your laughter is the melody that dances through my soul, a symphony of joy that fills the chambers of my heart.",
          "If our love were a river, it would flow endlessly, carving a path through the mountains of time, unstoppable and eternal.",
          "Your eyes are the windows to a world of wonder, a universe of endless possibilities that I long to explore.",
          "If I were a poet, I’d pen a thousand sonnets, each line a tribute to the enchanting spell you’ve cast upon me.",
          "Your touch is like a gentle breeze, caressing my skin and awakening my senses, a testament to the power of your love.",
          "In the garden of my heart, you are the most exquisite flower, a rare and precious bloom that I will cherish forever.",
          "Your love is the compass that guides me, a true north that leads me to the shores of happiness and contentment.",
          "If I could capture the essence of your beauty, I’d bottle it and wear it as a perfume, a fragrant reminder of your enchanting presence.",
          "Your voice is the sweetest lullaby, a soothing balm that calms the tempest of my soul and lulls me into a state of blissful serenity.",
          "If our love were a tapestry, it would be woven with threads of gold and silver, a masterpiece of passion and devotion.",
          "Your smile is the sun that breaks through the clouds, a radiant beam of light that warms my heart and brightens my day.",
          "If I were a sculptor, I’d chisel your likeness in marble, a timeless tribute to the beauty that has captured my heart.",
          "Your love is the key that unlocks the treasure chest of my heart, revealing a bounty of affection and adoration.",
          "Like a butterfly emerging from its cocoon, your love has transformed me, awakening a newfound sense of wonder and joy.",
          "If I could pluck the stars from the sky, I’d arrange them in a constellation that spells your name, a celestial tribute to your radiant beauty.",
          "Your presence is like a warm embrace on a cold winter’s night, a comforting haven that shelters me from the chill of loneliness.",
          "If our love were a symphony, it would be a crescendo of passion and emotion, a masterpiece that resonates through the ages.",
          "Your eyes are like twin galaxies, swirling with the mysteries of the universe, drawing me into their celestial embrace.",
          "If I could harness the power of the wind, I’d send a gentle breeze to whisper my love for you in your ear.",
          "Your love is the flame that ignites my soul, a burning passion that consumes me and sets my heart ablaze.",
          "If I were a painter, I’d create a masterpiece with your beauty as my muse, a portrait of perfection that captures your essence.",
          "Your touch is like a summer rain, a gentle caress that quenches my thirst and soothes my parched heart.",
          "If our love were a dance, it would be a waltz of passion and grace, a timeless expression of our devotion to one another.",
          "Your laughter is the song of angels, a heavenly chorus that lifts my spirits and fills my heart with joy.",
          "If I could pluck the petals of a thousand roses, I’d create a path for you to walk upon, a fragrant tribute to your captivating charm.",
          "Your touch is like a silken caress, a tender embrace that envelops me in a cocoon of warmth and affection.",
          "If our love were a garden, it would be a paradise of vibrant blooms, a sanctuary of peace and tranquility.",
          "Your smile is the rainbow that appears after the storm, a brilliant arc of color that brightens my world.",
          "If I could write a novel, it would be an epic tale of our love, a timeless story of passion and devotion.",
          "Your eyes are the mirrors of my soul, reflecting the depth of my love and the intensity of my desire.",
          "If I could traverse the heavens, I’d pluck the most radiant star and present it to you as a token of my undying love.",
          "Your love is the elixir that breathes life into my weary soul, a potion of passion that rejuvenates my heart.",
          "If I could traverse the depths of the ocean, I’d collect the rarest pearls to adorn you, a symbol of the precious treasure you are to me.",
          "Your embrace is like a warm blanket on a frosty night, enveloping me in a cocoon of comfort and affection.",
          "If our love were a melody, it would be a sultry jazz tune, a seductive dance of passion and desire.",
          "Your eyes sparkle like the finest champagne, intoxicating me with their effervescent allure.",
          "If I could command the elements, I’d summon a gentle rain to caress your skin, each droplet a tender kiss from the heavens.",
          "Your laughter is the chime of windchimes, a delicate symphony that fills the air with enchantment and delight.",
          "If I could weave a spell, I’d conjure a magical realm where we could dance among the stars, our love transcending time and space.",
          "Your touch is like the brush of a master artist, painting my heart with the vibrant hues of passion and desire.",
          "If our love were a flame, it would burn with the intensity of a thousand suns, an inferno of devotion that consumes us both.",
          "Your lips are like the petals of a delicate rose, their softness beckoning me to taste their sweet nectar.",
          "If I could harness the power of the moon, I’d bathe you in its silvery glow, illuminating your ethereal beauty.",
          "Your presence is like the first light of dawn, a radiant beam that dispels the shadows and fills my world with hope.",
          "If I could write a love letter to the universe, I’d pen an ode to your enchanting allure, a testament to the spell you’ve cast upon me.",
          "Your voice is the whisper of the wind, a gentle caress that stirs my soul and awakens my deepest desires.",
          "If our love were a garden, it would be a lush oasis, a sanctuary of passion and pleasure where we could lose ourselves in each other’s embrace.",
          "Your smile is the shimmer of sunlight on water, a dazzling display that captivates me and leaves me breathless.",
          "If I could compose a symphony, I’d dedicate each note to the rhythm of your heartbeat, a musical tribute to our love’s harmony.",
          "If I had a dollar for every mistake you did, I would have only one, because your entire life is a continuous mistake",
          "The sun shines upon your beautiful face from dusk till dawn, but my love outshines the sun from dusk till dawn and far beyond that"
      ])
      await self.highrise.chat(f": {user.username} - {poeticrizz}")

    if "Rizz" in message:
      pickuplines = random.choice([
          "Do you believe in love at first sight, or should I walk by again?",
          "Is your name Google? Because you have everything I've been searching for.",
          "Are you a magician? Whenever I look at you, everyone else disappears.",
          "Do you have a map? I keep getting lost in your eyes.",
          "Do you have a name, or can I call you mine?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "I must be a snowflake because I've fallen for you.",
          "Excuse me, but I think you dropped something: my jaw.",
          "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
          "Is your dad a boxer? Because you're a knockout!",
          "Do you have a map? I keep getting lost in your eyes.",
          "Is your name Google? Because you've got everything I've been searching for.",
          "Do you have a name, or can I call you mine?",
          "Are you a magician? Whenever I look at you, everyone else disappears.",
          "Is your name Wi-Fi? Because I'm feeling a connection.",
          "Do you have a sunburn, or are you always this hot?",
          "Excuse me, but I think you dropped something: my jaw.",
          "Is your dad a boxer? Because you're a knockout!",
          "If you were a vegetable, you'd be a cute-cumber.",
          "I must be a snowflake because I've fallen for you.",
          "Is your name Google? Because you've got everything I've been searching for.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Are you a magician? Every time I look at you, everyone else disappears.",
          "Do you believe in love at first sight, or should I walk by again?",
          "Excuse me, but I think you dropped something: my jaw.",
          "Is your name Wi-Fi? Because I'm feeling a connection.",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Can I follow you home? Cause my parents always told me to follow my dreams.",
          "Is your dad a boxer? Because you're a knockout!",
          "Do you have a name, or can I call you mine?",
          "I hope you know CPR, because you just took my breath away!",
          "So, aside from taking my breath away, what do you do for a living?",
          " I ought to complain to Spotify for you not being named this week’s hottest single.",
          "Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.",
          "Is your name Google? Because you've got everything I've been searching for.",
          "Can I follow you home? Cause my parents always told me to follow my dreams.",
          "Do you believe in love at first sight, or should I walk by again?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Is your dad a boxer? Because you're a knockout!",
          "Are you a magician? Because every time I look at you, everyone else disappears.",
          "Excuse me, but I think you dropped something: my jaw.",
          "If you were a triangle, you'd be acute one.",
          "Can I take you out for coffee, or do you prefer to brew it yourself?",
          "Are you made of copper and tellurium? Because you're Cu-Te.",
          "Are you a camera? Because every time I look at you, I smile.",
          "Do you have a name, or can I call you mine?",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "I must be a snowflake because I've fallen for you.",
          "I must be a magician because every time I look at you, everyone else disappears.",
          "Do you have a Band-Aid? I just scraped my knee falling for you.",
          "Are you a Wi-Fi signal? Because I'm feeling a connection.",
          "Do you believe in fate? Because I think we were meant to meet.",
          "Are you a time traveler? Because I can see you in my future.",
          "Do you have a name, or can I call you mine?",
          "Can I borrow a kiss? I promise I'll give it back.",
          "I must be a snowflake because I've fallen for you.",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Are you a campfire? Because you're hot and I want s'more.",
          "Can I take you out for coffee, or do you prefer to brew it yourself?",
          "Is your dad a boxer? Because you're a knockout!",
          "Is your name Ariel? Because we mermaid for each other!",
          "I'm not a photographer, but I can picture us together.",
          "Do you have a name, or can I call you mine?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "If you were a fruit, you'd be a fine-apple.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Do you believe in love at first sight, or should I walk by again?",
          "I must be a snowflake because I've fallen for you.",
          "Is your dad a boxer? Because you're a knockout!",
          "Are you a magician? Because whenever I look at you, everyone else disappears.",
          "Can I follow you home? Cause my parents always told me to follow my dreams.",
          "Do you have a name, or can I call you mine?",
          "Are you an interior decorator? When I saw you, the entire room became beautiful.",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Do you believe in love at first sight, or should I walk by again?",
          "Are you a Wi-Fi signal? Because I'm feeling a connection.",
          "Are you a time traveler? Because I can see you in my future.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Can I borrow a kiss? I promise I'll give it back.",
          "If you were a triangle, you'd be acute one.",
          "I must be a magician because every time I look at you, everyone else disappears.",
          "Do you have a Band-Aid? I just scraped my knee falling for you.",
          "Are you a campfire? Because you're hot and I want s'more.",
          "Can I take you out for coffee, or do you prefer to brew it yourself?",
          "Is your dad a boxer? Because you're a knockout!",
          "Is your name Ariel? Because we mermaid for each other!",
          "I'm not a photographer, but I can picture us together.",
          "Do you have a name, or can I call you mine?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "If you were a fruit, you'd be a fine-apple.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Do you believe in love at first sight, or should I walk by again?",
          "I must be a snowflake because I've fallen for you.",
          "Is your dad a boxer? Because you're a knockout!",
          "Are you a magician? Because whenever I look at you, everyone else disappears.",
          "Can I follow you home? Cause my parents always told me to follow my dreams.",
          "Do you have a name, or can I call you mine?",
          "Are you an interior decorator? When I saw you, the entire room became beautiful.",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Do you believe in love at first sight, or should I walk by again?",
          "Are you a Wi-Fi signal? Because I'm feeling a connection.",
          "Are you a time traveler? Because I can see you in my future.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Can I borrow a kiss? I promise I'll give it back.",
          "If you were a triangle, you'd be acute one.",
          "I must be a magician because every time I look at you, everyone else disappears.",
          "Do you have a Band-Aid? I just scraped my knee falling for you.",
          "Are you a campfire? Because you're hot and I want s'more.",
          "Can I take you out for coffee, or do you prefer to brew it yourself?",
          "Is your dad a boxer? Because you're a knockout!",
          "Is your name Ariel? Because we mermaid for each other!",
          "I'm not a photographer, but I can picture us together.",
          "Do you have a name, or can I call you mine?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "Do you believe in love at first sight, or should I walk by again?",
          "Are you a Wi-Fi signal? Because I'm feeling a connection.",
          "Are you a time traveler? Because I can see you in my future.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Can I borrow a kiss? I promise I'll give it back.",
          "If you were a triangle, you'd be acute one.",
          "I must be a magician because every time I look at you, everyone else disappears.",
          "Do you have a Band-Aid? I just scraped my knee falling for you.",
          "Are you a campfire? Because you're hot and I want s'more.",
          "Can I take you out for coffee, or do you prefer to brew it yourself?",
          "Is your dad a boxer? Because you're a knockout!",
          "Is your name Ariel? Because we mermaid for each other!",
          "I'm not a photographer, but I can picture us together.",
          "Do you have a name, or can I call you mine?",
          "If you were a vegetable, you'd be a cute-cumber.",
          "If you were a fruit, you'd be a fine-apple.",
          "Do you have a map? Because I keep getting lost in your eyes.",
          "Do you believe in love at first sight, or should I walk by again?",
          "I must be a snowflake because I've fallen for you.",
          "Is your dad a boxer? Because you're a knockout!",
          "If you hate me don't read this...Ok done it means you love me and I love you too congratulations we are in relationship...",
          "i may not be a dentist but...I'll surely take care of that smile of yours",
          "I don't have many pick up lines because I'm not trynna pick you up but pin you down",
          "i love people with humor but i love hu-mor (humor rizz)",
          "Are you a piano? Because I wanna use my fingers to play with you until you make beautiful noise!!!!!!!",
          "Texting isn't enough I need you sitting on My lap facing me",
          "Are you other peoples opinion? Cause I can't stop thinking about you (Social anxiety rizz)",
          "Are u lamp of Aladin bcoz i wanna rub u down there and get all my wishes complete",
          "Im glad you dad didn't pull out you're kinda Cool",
          "The word of the day is 'LEGS' So why don't you come over and we can spread the word",
          "I just wish I had more money instead of this massive cock.",
          "Do yk the difference between history and you? History is the past & you are my future (History Rizz)",
          "Are u the clock at school? Because I be lookin at u all day. (School clock rizz)",
          "Are you a painting? Because i'd like to pin you against my wall (artist rizz)",
          "Are you a box of chocolates? Cause I want to take your top off and eat you all night.",
          "Math is incorrect they keep talking about x and y instead of u and i (algebraic rizz)",
          "Why does everything have to be a relationship, We can't kiss and be friends?",
          "In honor of pride month maz How about you let me She/Them T!ddies",
          "I just say 'night' because if it was goodnight you'd be in my bed",
          "You look kinda ill, you must be suffering from a lack of 'Vitamin ME'",
          "Did you know that sleeping next to the person you like helps you fall asleep faster, reduces depression and makes you live longer so why aren't you here every night?"
      ])
      await self.highrise.chat(f": {user.username} - {pickuplines}")

    if "Joke" in message or "joke" in message:
      joke = random.choice([
          "Yo mama's so fat, when she goes camping, the bears hide their food.",
          "Your mama's so fat she falls both sides of the bed",
          "I wont tell ya lol",
          "Your mama's so stupid she studied for COVID test",
          "Your mama so ugly when she goes to the dentist they make her lay face down",
          "Your mama's so stupid she used a ruler to see how long she slept",
          "Your mama's so fat her belt size is the size of the equator",
          "Your mama's so ugly when she falls of the car, the driver gets arrested for littering",
          "I told my wife she was drawing her eyebrows too high. She looked surprised.",
          "Why don't scientists trust atoms? Because they make up everything.",
          "What do you call fake spaghetti? An impasta.",
          "Why don't skeletons fight each other? They don't have the guts.",
          "I used to play piano by ear, but now I use my hands.",
          "I'm on a whiskey diet. I've lost three days already.",
          "What do you call a bear with no teeth? A gummy bear.",
          "I told my wife she was drawing her eyebrows too low. She looked surprised.",
          "The early bird might get the worm, but the second mouse gets the cheese.",
          "Parallel lines have so much in common. It's a shame they'll never meet.",
          "Why don't seagulls fly over the bay? Because then they'd be bagels.",
          "How do you organize a space party? You planet.",
          "Did you hear about the kidnapping at the playground? They woke up.",
          "My boss told me to have a good day, so I went home.",
          "Joke? Your whole life",
          "i just found out if two girls are close, their period dates can change to be at the same time, tf kinda bluetooth is that",
          "Remember if there's ever a person you like and are talking to, you should just cut off contact and block them because it's never gonna work",
          "Nah cuz why tf do girls make code names for boys. Like who tf is 'Pineapple'"
      ])
      await self.highrise.chat(f": {user.username} - {joke}")

    if "Funfact" in message or "funfact" in message:
      funfact = random.choice([
          "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs over 3,000 years old.",
          "Bananas are berries, while strawberries are not technically berries but aggregate fruits.",
          "The Eiffel Tower can grow up to 6 inches taller during the summer due to thermal expansion.",
          "Humans and giraffes have the same number of neck vertebrae—seven.",
          "Octopuses have three hearts.",
          "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted just 38 minutes.",
          "The Great Wall of China is not visible from space with the naked eye.",
          "The Hawaiian alphabet has only 12 letters: A, E, I, O, U, H, K, L, M, N, P, and W.",
          "A group of flamingos is called a 'flamboyance.'",
          "The tongue is the only muscle in the human body that is attached at only one end.",
          "The average person will spend six months of their life waiting for red lights to turn green.",
          "A group of crows is called a 'murder.'",
          "The world's oldest known recipe is for beer and dates back over 4,000 years.",
          "A day on Venus is longer than a year on Venus. It takes about 243 Earth days for Venus to complete one rotation but only 225 Earth days to orbit the Sun.",
          "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted just 38 minutes.",
          "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo.'",
          "The unicorn is the national animal of Scotland.",
          "The average person will walk the equivalent of three times around the world in their lifetime.",
          "Cows have best friends and get stressed when they are separated.",
          "The longest time between two twins being born is 87 days.",
          "Astronauts cannot burp in space due to the absence of gravity.",
          "A hummingbird weighs less than a penny.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Slugs have four noses.",
          "Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.",
          "The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.",
          "The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.",
          "The first alarm clock could only ring at 4 a.m.",
          "A crocodile's tongue is attached to the roof of its mouth and cannot move.",
          "Sea otters hold hands while sleeping to avoid drifting apart.",
          "The electric chair was invented by a dentist.",
          "The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.",
          "Some people can unfocus their eyesight (or make their eyesight blurry) on command",
          "Making fun of a short girls height is indirectly telling her that you are in love with her 😭",
          "No matter how wrong she is, if she is short, forgive her. She is just a baby",
          "If you see my typing for to long, just gimme time cuz I'm either tryna find a emoji or spell a word correctly.",
          "you know your friendship elite if it started with 'when I first met you i didn't like you' ",
          "Life is too short to argue just blame your sister for everything and move on",
          "If you are dead inside, go outside ",
          "If she has strict parents,back problems,stays on her phone all day,and gets mad and jealous over the little things and she's 5'0-5'6ft ,Wife her asap",
          "Girls will never admit they like u lol either they text u all day, call you sir or bro, or post stuff on their story hoping you'll slide up",
          "Never trust girls, they screenshot your messages and laugh at u with their friends",
          "Instead of typing 'lol' or 'lmao' imma start using 'salts' which stands for Smiled A Little Then Stopped. It's way more accurate",
          "When i say 'I hate drama' I mean I hate being involved in drama. Other people's drama On the other hand? Huge fan",
          "If a boy cries for you keep him. But if a girl cries for you, it doesn't matter, she always cries",
          "Girls need to realize that if they make the first move they have a 99,9% success rate"
      ])
      await self.highrise.chat(f": {user.username} - {funfact}")

    if "Roastme" in message or "roastme" in message or "roast" in message:
      roastme = random.choice([
          "Oh, look who finally decided to show up on time! Did you have to invent a new way of setting your alarm?",
          "I heard you attempted cooking last night. How many smoke alarms did you set off this time?",
          "You're always talking about how organized you are, but have you seen your desk? It's a masterpiece of chaos!",
          "Are you wearing sunglasses indoors because you're a celebrity, or is it just to hide those tired eyes?",
          "I can't believe how much you love coffee. Is it your lifeline, or did you just marry a coffee machine?",
          "You know, I envy your ability to take naps anywhere. I'm starting to think you might be part cat.",
          "I heard you tried singing in the shower again. Next time, let me know so I can bring some earplugs!",
          "Your texting speed is impressive – I'm pretty sure your thumbs have their own gym membership.",
          "I think your fashion sense is ahead of its time. It's like you're living in the year 3010!",
          "You have such a great sense of direction. As long as we're not trying to get somewhere, we'll be fine!",
          "If genius skips a generation, your children will be brilliant.",
          "Whatever doesn’t kill you, disappoints me.",
          "You’re my favorite person… besides every other person I’ve ever met. ",
          "I hope your wife brings a date to your funeral.",
          "You’re about as useful as a screen door on a submarine.",
          "If you were an inanimate object, you’d be a participation trophy.",
          "I can’t wait to spend my whole life without you.",
          "Take my lowest priority and put yourself beneath it.",
          "You are what happens when women drink during pregnancy.",
          "I don’t hate you, but if you were drowning, I would give you a high five.",
          "Were you born on the highway? That is where most accidents happen.",
          "Unless your name is Google, stop acting like you know everything!",
          "I didn’t mean to offend you… but it was a huge plus.",
          "There is someone out there for everyone. For you, it’s a therapist.",
          "Sorry I can’t think of an insult dumb enough for you to understand.",
          "You are the sun in my life… now get 93 million miles away from me.",
          "I would smack you, but I’m against animal abuse.",
          "I don’t know what makes you so stupid, but it works.",
          "That sounds like a you problem.",
          "I believed in evolution until I met you.",
          "Whoever told you to be yourself, gave you a bad advice.",
          "You have such a beautiful face… But let’s put a bag over that personality.",
          "I envy people who have never met you.",
          "If I throw a stick, will you leave me too?",
          "I don’t have the time or the crayons to explain this to you.",
          "You’re impossible to underestimate.",
          "People like you are the reason God doesn’t talk to us anymore.",
          "When I look at you, I wish I could meet you again for the first time… and walk past.",
          "You are a pizza burn on the roof of the world’s mouth.",
          "You're so ugly Santa goes ho ho holy shit!",
          "You're so ugly Bob the builder took one look and said we can't fix that",
          "You're so ugly that when you were born the doctor slapped both your parents",
          "You're so ugly your birth certificate is just an apology",
          "You're like the end the end pieces of a loaf of bread,Everybody touches you but nobody wants you ",
          "I hope you loose weight so there'll be less of youWhere is your off button?",
          "I know you don't like me, and that implies you need better taste.",
          "I'm no an astronomer, but I'm pretty sure the Earth revolves around the sun… not you.",
          "I'd give you a nasty look, but it seems like you've already got one.",
          "Your birth certificate should be rewritten as a letter of apology ",
          "You haven't changed since the last time I saw you. You really should. ",
          "Your bad personality is the reason I prefer animals to humans.",
          " You hear that? It's the sound of me not caring. ",
          "I might be fully vaccinated, but I'm still not going to hang out with you.",
          "You're so annoying, you could make a Happy Meal cry.",
          "Oh, sorry, did the middle of my sentence interrupt the beginning of yours?",
          "You know, you're just not pretty enough to have such an ugly personality.",
          "You just might be why the middle finger was invented in the first place.",
          "You have a face that makes onions cry.",
          "Have a nice day… somewhere else.",
          "You do realize we're just tolerating you, right? ",
          "Were you born this stupid or did you take lessons?",
          "It's really fun watching you try to understand everything that's being said about you.",
          "You are even more useless than the 'ueue' in queue.",
          "The real heroes in this world are the ones who have to live with you.",
          "Somewhere out there a tree is producing oxygen for you. What a shame.",
          "Everyone is allowed to act stupid once in a while, but you're really abusing the privilege.",
          "If you're going to be two-faced, at least make one of them pretty.",
          "I was today years old when I realized I didn't like you.",
          "I'm not a nerd; I'm just smarter than you.",
          " If I had a dollar every time you shut up, I would give it back as a thank you.",
          "I didn't mean to offend you… but I'll take it as an additional perk.",
          "I don't want to rain on your parade. I want to summon a typhoon.",
          "You can't imagine how much happiness you can bring… by leaving the room. ",
          "I've been called worse things by better men.",
          "I didn't mean to push your buttons, I was just looking for mute.",
          "I forgot the world revolves around you. My apologies! How silly of me.",
          "I'd rather treat a baby's diaper rash than have lunch with you.",
          "I would smack you, but I'm against animal abuse.",
          "I gave out all my trophies a while ago, but here's a participation award.",
          "It's all about balance… you start talking, I stop listening.",
          "You're the reason this country has to put directions on shampoo bottles.",
          "How many licks 'till I get to the interesting part of this conversation?",
          "When you start talking, I stop listening.",
          "I'm listening. I just need a minute to process so much stupid information at once.",
          "You are like a software update. Every time I see you, I immediately think 'not now.",
          "Don't worry… the first 40 years of childhood are always the hardest.",
          "It's impossible to underestimate you.",
          "I like the way you comb your hair. It's impressive how you're able to hide the horns.",
          "If I throw a stick, will you chase it? I really want out of this conversation.",
          "You're the reason gene pools need lifeguards.",
          "I don't know what makes you so stupid, but it's really doing the job.",
          "The truth will set you free. You're the worst. OK, you're free to go.",
          "Do you think your parents realize that they're living proof that two wrongs don't make a right?",
          "Give me a minute; I'm trying to think of an insult simple enough for you to understand!",
          "I know our son got his brains from you because, well, I still have mine.",
          "I've heard a smarter statement come out in a fart.",
          "I look at you and think… two billion years of evolution for this?",
          "I told my therapist about you. She didn't believe me.",
          "Don't be ashamed of who you are. That's a job for your parents.",
          "When I listen to you, I think you really are going to go far. I hope you stay there.",
          "When I see you coming, I get pre-annoyed. I figure it's smart to give myself a head start.",
          "Whoever told you to be yourself gave you bad advice.",
          "I think you just need a high five… in the face… with a chair.",
          "When I look at you, I think to myself where have you been my whole life? And can you go back there?",
          "Light travels faster than sound. It explains why you seemed smart… until I finally heard you speak.",
          "Your secrets are always safe with me. I don't even listen when you share them.",
          "When God made you, you must have been on the bottom of his 'to-do' list.",
          "Everyone brings happiness to a room. I bring happiness when I walk in, and you bring happiness when you leave.",
          "Sweetheart, the only thing bothering me is that thing between your ears.",
          "Your face is fine, but you really should put a bag over that personality.",
          "I would call you an idiot, but it would be an insult to stupid people.",
          "Are you at a loss for words, or did you exhaust your entire vocabulary?",
          "Accidents happen; the proof is sitting right there.",
          "You bring everyone so much joy… when you leave the room.",
          "You're not simply a drama queen. You're the whole royal family.",
          "You're like a gray sprinkle on a rainbow cupcake.",
          " You are more disappointing than an unsalted pretzel. ",
          "I can't wait to spend my whole life without you.",
          "Rolling your eyes isn't going to help you find your brain. ",
          "It’s not that you’re annoying; it’s just that I’d linken you to the human version of period cramps.",
          "You are gay,go back to your default setting",
          "Roses are red Voilets are blue,Faces like yours Belong in the zoo,Don't be mad I'll be there too,Not in the cage But laughing at you..",
          "Even potatoes are getting smashed but you're not"
      ])
      await self.highrise.chat(f": {user.username} - {roastme}")

    if "Deathyear" in message or "deathyear" in message:
      death_year = random.randint(2023, 2100)
      await self.highrise.chat(f" {user.username} IDK when you would die but maybe around: {death_year}")

    if "weddingyear" in message or "Weddingyear" in message:
      death_year = random.randint(2023, 2040)
      await self.highrise.chat(f"{user.username} IDK when will the wedding take place but maybe around: {death_year} Enjoy🌚")

    

  async def stop_continuous_emote(self, user_id: int):
    if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[
        user_id].cancelled():
      task = self.continuous_emote_tasks[user_id]
      task.cancel()
      with contextlib.suppress(asyncio.CancelledError):
        await task
      del self.continuous_emote_tasks[user_id]

  async def send_continuous_emote(self, emote_id: str, user_id: int,
                                  delay: float):
    try:
      while True:
        await self.highrise.send_emote(emote_id, user_id)
        await asyncio.sleep(delay)
    except ConnectionResetError:
      print(
          f"Failed to send continuous emote to user {user_id}. Connection was reset."
      )
    except asyncio.CancelledError:
      print(f"Continuous emote task for user {user_id} was cancelled.")
    except ResponseError as error:
      if str(error) == "Target user not in room":
        print(f"User {user_id} is not in the room.")
      else:
        raise  # Re-raise the exception if it's not the one we're handling.

  async def send_random_reactions(self,
                                  user_id: str,
                                  num_reactions: int = 1,
                                  delay: float = 1.1) -> None:
    reactions = ["heart", "wink", "wave", "thumbs", "clap"]
    for _ in range(num_reactions):
      reaction = random.choice(reactions)
      await self.highrise.react(reaction, user_id)
      await asyncio.sleep(delay)  # Add a delay between reactions
      
  async def teleport_user_next_to(self, target_username: str, requester_user: User):

        room_users = await self.highrise.get_room_users()
        requester_position = None

        for user, position in room_users.content:
          if user.id == requester_user.id:
              requester_position = position
              break
        for user, position in room_users.content:
          if user.username.lower() == target_username.lower(): 
            z = requester_position.z 
            new_z = z + 1 

            user_dict = {
              "id": user.id,
              "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
            }
            await self.highrise.teleport(user_dict["id"], user_dict["position"])

  async def follow_user(self, target_username: str):
    while self.following_username == target_username:
        # ابحث عن موقع المستخدم المستهدف في الغرفة
        response = await self.highrise.get_room_users()
        target_user_position = None
        for user_info in response.content:
            if user_info[0].username.lower() == target_username.lower():
                target_user_position = user_info[1]
                break

        if target_user_position:
            nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
            await self.highrise.walk_to(nearby_position)

            await asyncio.sleep(1)
 

  async def on_user_move(self, user: User, pos: Position) -> None:
    """On a user moving in the room."""
    if user.username in self.allowed_usernames:
      print(user.username, pos)

  async def follow_dm(self, roomId: str) -> None:
    last_id = ''
    conversation_ids = []
    response = await self.highrise.get_conversations()
    conversations = response.conversations

  # loop through the conversations and send a room invite in each conversation
    while len(conversations) > 0:
      print(len(conversations))

      for conversation in conversations:
        conversation_ids.append(conversation.id)
        last_id = conversation.id
        print(f"Invite Sent {last_id}")

    # get next set of conversations
      response = await self.highrise.get_conversations(False, last_id)
      conversations = response.conversations

    for conversation_id in conversation_ids:
      await self.highrise.send_message(conversation_id, "𝙅𝙤𝙞𝙣 𝙂𝙞𝙫𝙚𝙖𝙬𝙖𝙮 𝘼𝙣𝙙 𝙒𝙞𝙣 𝙀𝙥𝙞𝙘 𝘾𝙝𝙚𝙘𝙠 𝙤𝙪𝙩 @iZexy 𝙋𝙤𝙨𝙩 𝙁𝙤𝙧 𝙢𝙤𝙧𝙚 𝙙𝙚𝙩𝙖𝙞𝙡𝙨❤️")

  async def send_invite_to_all_conversations(self, roomId: str) -> None:
    last_id = ''
    conversation_ids = []
    response = await self.highrise.get_conversations()
    conversations = response.conversations

  # loop through the conversations and send a room invite in each conversation
    while len(conversations) > 0:
      print(len(conversations))

      for conversation in conversations:
        conversation_ids.append(conversation.id)
        last_id = conversation.id
        print(f"Invite Sent {last_id}")

    # get next set of conversations
      response = await self.highrise.get_conversations(False, last_id)
      conversations = response.conversations

    for conversation_id in conversation_ids:
      await self.highrise.send_message(conversation_id, "Join my room!", "invite", roomId)

  async def emote_loop(self):
    while True:
        await self.highrise.send_emote(
            random.choice([
              "idle-loop-sitfloor", "emote-tired", "emote-pose7", "emoji-thumbsup",
              "emoji-angry", "dance-macarena", "emote-hello", "dance-weird",
              "emote-superpose", "idle-lookup", "idle-hero", "emote-wings",
              "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes",
              "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull",
              "emote-think", "emote-hot", "dance-shoppingcart", "emote-greedy",
              "emote-frustrated", "emote-float", "emote-baseball", "emote-yes",
              "idle_singing", "idle-floorsleeping", "idle-loop-sitfloor",
              "idle-enthusiastic", "emote-confused", "emoji-celebrate", "emote-no",
              "emote-swordfight", "emote-shy", "dance-tiktok2", "emote-model",
              "emote-charging", "emote-snake", "dance-russian", "emote-sad",
              "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging",
              "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow",
              "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
              "idle-dance-tiktok4"
              "emote-maniac", "emote-energyball", "emote-frog", "emote-cute",
              "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8",
              "idle-dance-casual", "emote-pose1", "dance-sexy", "emote-pose3",
              "emote-pose5", "emote-cutey", "emote-Relaxing", "emote-model",
              "emote-fashionista", "emote-gravity", "emote-zombierun",
              "emoji-ceilebrate", "emoji-floss", "emote-Relaxing ", "emote-punkguitar",
              "dance-tiktok9", "dance-weird", "emote-punkguitar", "idle-uwu"
              "emote-swordfight", "emote-handstand", "emote-bow", "emote-cursty",
              "dance-breakdance", "emote-creepycute", "emote-headblowup", "idle-guitar",
                # ... (add your emote choices here)
            ]))
        await asyncio.sleep(4)

  async def quotes_loop(self):
    try:
        with open('quotes.json', 'r') as f:
            file_content = f.read()
            if not file_content.strip():
                print("Warning: 'quotes.json' is empty or contains only whitespace.")
                return

            quotes = json.loads(file_content)

        while True:
            data = random.choice(quotes)
            note_text = data["quote"] + " " + data["emoji"]
            await self.highrise.chat(note_text)
            await asyncio.sleep(75)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in 'quotes.json': {e}")
        # Handle the error as needed, e.g., by providing a default value or terminating the loop.

  async def is_new_user(self, user: User) -> bool:
    try:
      data = db[user.id]
      print(f"{user.username} is in the database:: {data}")
      if data['tipped']:
        return False
      else:
        return True
    except:
      return True

  async def tip_new_user(self, user: User, amount: int) -> None:
    if await self.is_new_user(user):
      #check if the bot has the amount
      bot_wallet = await self.highrise.get_wallet()
      bot_amount = bot_wallet.content[0].amount
      if bot_amount <= amount:
        print(f"Not enough funds")
        return

      #converts the amount to a string of bars and calculates the fee
      """Possible values are: "gold_bar_1",
      "gold_bar_5", "gold_bar_10", "gold_bar_50", 
      "gold_bar_100", "gold_bar_500", 
      "gold_bar_1k", "gold_bar_5000", "gold_bar_10k" """
      bars_dictionary = {
          10000: "gold_bar_10k",
          5000: "gold_bar_5000",
          1000: "gold_bar_1k",
          500: "gold_bar_500",
          100: "gold_bar_100",
          50: "gold_bar_50",
          10: "gold_bar_10",
          5: "gold_bar_5",
          1: "gold_bar_1"
      }
      fees_dictionary = {
          10000: 1000,
          5000: 500,
          1000: 100,
          500: 50,
          100: 10,
          50: 5,
          10: 1,
          5: 1,
          1: 1
      }
      #loop to check the highest bar that can be used and the amount of it needed
      tip = []
      total = 0
      for bar in bars_dictionary:
        if amount >= bar:
          bar_amount = amount // bar
          amount = amount % bar
          for i in range(bar_amount):
            tip.append(bars_dictionary[bar])
            total = bar + fees_dictionary[bar]
      if total > bot_amount:
        print(f"Not enough funds")
        return
      for bar in tip:
        await self.highrise.tip_user(user.id, bar)
        db[user.id] = {'tipped': True}
        print(f"tipping {user.username} {bar}")
        
    else:
      print(f"{user.username} has already been tipped")

  async def dance_sequence(self, user):
    emotes = ["dance-employee", "emote-pose6", "emote-celebrationstep", "emote-stargazer", "idle-nervous", "emote-sleigh", "sit-relaxed", "dance-pinguin", "idle-dance-casual", "idle_singing", "dance-tiktok8", "dance-tiktok2",  "dance-icecream", "dance-anime", "emote-astronaut", "emote-pose9", "emote-boxer", "idle-guitar", "dance-anime", "dance-pinguin", "dance-creepypuppet", "emote-headblowup"]
    try:
        for emote in emotes:
            if self.stop_signal:  # Check if stop signal is set
                print("Dance sequence stopped.")
                break  # Break out of the loop if stop signal is set
            print(f"sending {emote} to {user.username}")
            await self.highrise.send_emote(emote, user.id)
            await asyncio.sleep(7)
    except Exception as e:
        print(f"Error: {e}")
