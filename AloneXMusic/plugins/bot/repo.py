from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
✪ 𝐖εℓ¢σмє 𝐅σя Stranger 𝐑єρσѕ ✪
 
 TERI MAAKICHUT REPO LEGA BHADWA... BAAP SE BOL KHUD BANA LE
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/e6471d19bd04a5095436a.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
