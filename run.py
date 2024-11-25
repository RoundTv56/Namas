from highrise.__main__ import *
from importlib import import_module
import time
import asyncio
import traceback
from keep_alive import keep_alive
import os

async def run_bot(bot, bot_name):
    while True:
        try:
            print(f"Running the {bot_name} loop")
            definitions = [bot]
            await main(definitions)
        except Exception as e:
            traceback.print_exc()
            print(f"An exception occurred for {bot_name}: {e}")
            await asyncio.sleep(5)
        finally:
            print(f"{bot_name} has stopped. Restarting in 5 seconds...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    # First bot details
    bot_file_name_1 = "main"
    bot_class_name_1 = "Bot"
    room_id_1 = "674471fd8fa43e92547d74a6"
    bot_token_1 = "62c10e9ddd744d57939d6c553e0e095619596617e5701c9c47ff2434213af4fb"   
    my_bot_1 = BotDefinition(getattr(import_module(bot_file_name_1), bot_class_name_1)(), room_id_1, bot_token_1)

    keep_alive()

    # Check if the watchdog script is not running for the first bot
    if not os.environ.get("REPL_WATCHDOG"):
        loop = asyncio.get_event_loop()
        task_1 = loop.create_task(run_bot(my_bot_1, "first bot"))

    # Run the event loop
    loop.run_until_complete(asyncio.gather(task_1))

