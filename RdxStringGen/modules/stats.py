from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from RdxStringGen import RDX
from RdxStringGen.utils import get_served_users


@RDX.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ {RDX.name} :\n\n {users} ᴜsᴇʀs")
