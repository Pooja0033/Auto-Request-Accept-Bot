import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "๐๐ผ๐ ๐ฆ๐๐ฎ๐ฟ๐๐ฒ๐ฑ ๐ฃ๐น๐ฒ๐ฎ๐๐ฒ ๐ฆ๐๐ฏ๐๐ฐ๐ฟ๐ถ๐ฏ๐ฒ ๐ข๐ฝ๐๐๐ง๐ฒ๐ฐ๐ต๐",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("๐๐ฟ๐ณ๐ฐ๐๐ด๐", url="https://t.me/kmtz_channel_v3"),
      InlineKeyboardButton("๐๐๐ฟ๐ฟ๐พ๐๐", url="https://t.me/kmtz_v4")
      ],[
      InlineKeyboardButton("Cแดษดแดแดแดแด Aแดแดษชษด", url=f"https://t.me/Owner_PM_Bot")
      ]]
    await message.reply_text(text="**๐ท๐ด๐ป๐ป๐พ...โก\n\n๐ธ๐ฐ๐ผ ๐ฐ ๐๐ธ๐ผ๐ฟ๐ป๐ด ๐๐ด๐ป๐ด๐ถ๐๐ฐ๐ผ ๐ฐ๐๐๐พ ๐๐ด๐๐๐ด๐๐ ๐ฐ๐ฒ๐ฒ๐ด๐ฟ๐ ๐ฑ๐พ๐.\n๐ต๐พ๐ ๐๐พ๐๐ ๐ฒ๐ท๐ฐ๐๐ ๐ฒ๐๐ด๐ฐ๐๐ด ๐พ๐ฝ๐ด ๐ฑ๐พ๐... \n๐๐ธ๐ณ๐ด๐พ ๐พ๐ฝ ๐ผ๐ ๐๐พ๐๐๐๐ฑ๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} ๐น๐พ๐ธ๐ฝ๐ด๐ณ โก") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("๐๐ผ๐ ๐ฆ๐๐ฎ๐ฟ๐๐ฒ๐ฑ ๐ฃ๐น๐ฒ๐ฎ๐๐ฒ ๐ฆ๐๐ฏ๐๐ฐ๐ฟ๐ถ๐ฏ๐ฒ ๐ข๐ฝ๐๐๐ง๐ฒ๐ฐ๐ต๐")
pr0fess0r_99.run()
