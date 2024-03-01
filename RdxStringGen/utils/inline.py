from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="˹ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ˼", callback_data="gensession")],
        [
            InlineKeyboardButton(text="˹sᴜᴘᴘ๏ꝛᴛ˼", url="https://t.me/+RObRa7kXPIJmMjU1"),
        [   InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛє˼", url="https://t.me/+m4oVCt2zFhYyMTdl"),][
            InlineKeyboardButton(
                text="˹๏ᴡɴєꝛ˼", user_id="1777270311"),
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="˹ᴩʏʀᴏɢʀᴀᴍ v1˼", callback_data="pyrogram1"),
            InlineKeyboardButton(text="˹ᴩʏʀᴏɢʀᴀᴍ v2˼", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="˹ᴛᴇʟᴇᴛʜᴏɴ˼", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="˹ᴛʀʏ ᴀɢᴀɪɴ˼", callback_data="gensession")]]
)
