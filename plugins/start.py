#please give credits https://github.com/MN-BOTS
#  @MrMNTG @MusammilN
from pyrogram import Client as MN_Bot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from verify_patch import IS_VERIFY, validate_token_and_verify, is_verified, build_verification_link, HOW_TO_VERIFY
from datetime import datetime

#please give credits https://github.com/MN-BOTS
#  @MrMNTG @MusammilN
class TEXT:
    START = """
<b>ɪ'ᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ!</b>

📥 ꜱᴇɴᴅ ᴍᴇ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.
⚠️ ᴏɴʟʏ ᴠɪᴅᴇᴏꜱ ᴜɴᴅᴇʀ 𝟸ɢʙ ᴀʀᴇ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.
📢 ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ.

"""
    DEVELOPER = "👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ"
    UPDATES_CHANNEL = "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ"
    SOURCE_CODE = "💬 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ"

class INLINE:
    START_BTN = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(TEXT.DEVELOPER, url="https://t.me/pArAd0X6")],
            [
                InlineKeyboardButton(TEXT.UPDATES_CHANNEL, url="https://t.me/world_0f_parad0x"),
                InlineKeyboardButton(TEXT.SOURCE_CODE, url="https://t.me/world_0f_parad0x"),
            ],
        ]
    )

#please give credits https://github.com/MN-BOTS
#  @MrMNTG @MusammilN
@MN_Bot.on_message(filters.command("start"))
async def start(client: MN_Bot, message: Message):
    user_id = message.from_user.id
    args = message.text.split()

    # Handle verification token in /start parameter
    if len(args) > 1 and args[1].startswith("verify_"):
        token = args[1].split("_", 1)[1]
        if await validate_token_and_verify(user_id, token):
            await message.reply_text("✅ ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪғɪᴇᴅ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ ғᴏʀ 𝟷𝟸 ʜᴏᴜʀꜱ.")
        else:
            await message.reply_text("❌ ɪɴᴠᴀʟɪᴅ ᴏʀ ᴇxᴘɪʀᴇᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ʟɪɴᴋ.")
        return

    user = message.from_user
    mention = user.mention
    await message.reply_text(
        TEXT.START,
        disable_web_page_preview=True,
        reply_markup=INLINE.START_BTN,
    )

#please give credits https://github.com/MN-BOTS
#  @MrMNTG @MusammilN
