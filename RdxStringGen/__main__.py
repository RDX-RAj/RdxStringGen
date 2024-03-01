import asyncio
import importlib

from pyrogram import idle

from RdxStringGen import LOGGER, RDX
from RdxStringGen.modules import ALL_MODULES


async def rdx_boot():
    try:
        await RDX.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("RdxStringGen.modules." + all_module)

    LOGGER.info(f"@{RDX.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(rdx_boot())
    LOGGER.info("Stopping String Gen Bot...")
