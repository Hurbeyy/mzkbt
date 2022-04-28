# Size linkler halinde arar. 
import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["ara"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("𝐁𝐚𝐧𝐚 𝐒𝐚𝐧𝐚𝐭𝐜𝐢 𝐈𝐬𝐦𝐢 𝐘𝐚𝐝𝐚 𝐒𝐚𝐫𝐤𝐢 𝐈𝐬𝐦𝐢 𝐕𝐞𝐫𝐢𝐧 !")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("𝐀𝐫𝐢𝐲𝐨𝐫𝐮𝐦 ...")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"𝐈𝐬𝐢𝐦 - {results[i]['title']}\n"
            text += f"𝐒𝐮𝐫𝐞 - {results[i]['duration']}\n"
            text += f"𝐆𝐨𝐫𝐮𝐧𝐭𝐮𝐥𝐞𝐦𝐞 - {results[i]['views']}\n"
            text += f"𝐊𝐚𝐧𝐚𝐥 - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
