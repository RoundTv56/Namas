import asyncio
import json
import logging
import random
import time
import highrise
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
    TaskGroup,
)

EMOTE_LIST = ["emote-celebrate", "emote-launch", "emote-astronaut", "dance-pinguin", "dance-anime", "dance-creepypuppet",
              "emote-creepycute", "emote-shy2", "dance-touch", "dance-employee", "emote-zombierun", "emote-gravity",
              "dance-icecream", "dance-tiktok11", "emote-headblowup", "idle-guitar"]

DEFAULT_ENTITY_MIN_X = 7.5
DEFAULT_ENTITY_MAX_X = 12.5
DEFAULT_ENTITY_MIN_Y = 5.0
DEFAULT_ENTITY_MAX_Y = 5.0
DEFAULT_ENTITY_MIN_Z = 0.5
DEFAULT_ENTITY_MAX_Z = 3.5

DEFAULT_ENTITY_COORDINATES = (
    (DEFAULT_ENTITY_MIN_X + DEFAULT_ENTITY_MAX_X) / 2,
    (DEFAULT_ENTITY_MIN_Y + DEFAULT_ENTITY_MAX_Y) / 2,
    (DEFAULT_ENTITY_MIN_Z + DEFAULT_ENTITY_MAX_Z) / 2
)

def send_continuous_emotes(bot_instance):
    async def send_continuous_emotes():
        try:
            while True:
                room_users_response = await bot_instance.highrise.get_room_users()
                room_users = room_users_response.content
                emote = random.choice(EMOTE_LIST)
                emote_tasks = [send_emote_to_user(bot_instance, emote, user.id) for user, pos in room_users if is_user_in_specified_area(bot_instance, pos)]
                await asyncio.gather(*emote_tasks)
                await asyncio.sleep(9)
        except Exception as e:
            print(f"Error sending continuous emotes: {e}")

    asyncio.ensure_future(send_continuous_emotes())

async def send_emote_to_user(bot_instance, emote, user_id):
    try:
        await bot_instance.highrise.send_emote(emote, user_id)
    except highrise.ResponseError as e:
        if "Target user not in the room" in str(e):
            print(f"User with ID {user_id} left the room. Skipping emote.")
        else:
            print(f"Error sending emote to user with ID {user_id}: {e}")

def is_user_in_specified_area(bot_instance, pos):
    if pos is not None:
        if isinstance(pos, AnchorPosition):
            x, y, z = get_position_coordinates(bot_instance, pos)
        else:
            x, y, z = get_position_coordinates(bot_instance, pos)
            return (
                    bot_instance.AREA_MIN_X <= x <= bot_instance.AREA_MAX_X
                    and bot_instance.AREA_MIN_Y <= y <= bot_instance.AREA_MAX_Y
                    and bot_instance.AREA_MIN_Z <= z <= bot_instance.AREA_MAX_Z
            )
    return False

def get_position_coordinates(bot_instance, pos):
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