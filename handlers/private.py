from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Hehe tarafฤฑndan dรผzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""โ **๐ฌ๐พ๐๐๐บ๐ป๐บ** {message.from_user.mention} \n\nโ **๐ก๐พ๐** {bot} !\n\nโ **๐ฒ๐พ๐๐๐ ๐ฒ๐๐๐ป๐พ๐๐๐พ๐๐ฝ๐พ mรผzik ๐ข๐บ๐๐บ๐ป๐๐๐พ๐ ๐ก๐๐๐๐ . . !** \n\nโ **๐ก๐บ๐ ๐ธ๐พ๐๐๐๐๐๐, ๐ฒ๐พ๐ ๐ธ๐๐๐พ๐๐๐ ๐ธ๐พ๐๐๐๐๐ ๐๐พ๐๐๐ ๐ ๐๐๐๐๐บ๐๐ ๐ฆ๐๐๐ป๐บ ๐ค๐๐๐พ๐๐๐ . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ ๐๐๐ง๐ข ๐๐ซ๐ฎ๐๐ ๐๐ค๐ฅ๐ ๐", url=f"https://t.me/Globalvideo_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐น๐ท ๐๐ฌ๐ข๐ฌ๐ญ๐๐ง", url="https://t.me/Globalvideo_bot"
                    ),
                    InlineKeyboardButton(
                        "๐ ๐๐๐ฌ๐ญ๐๐ค", url="https://t.me/Ankara_Sohbet_Grubu"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐จ๐ฆ๐ฎ๐ญ๐ฅ๐๐ซ" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "๐ ๐๐๐ง๐๐ฅ", url=f"https://t.me/Ankara_sohbet_grubu"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("โ **๐ญ๐๐ :\n\n ๐ก๐๐๐๐ ๐ ๐๐๐๐ฟ ๐ข๐บ๐๐๐๐๐บ๐๐ ๐๐ผ๐๐ ๐ฒ๐ ๐ด๐ผ ๐๐พ๐๐๐๐๐พ ๐๐๐๐๐๐บ๐ผ๐ ๐ต๐บ๐๐ฝ๐๐ :\n\n> ๐ฌ๐พ๐๐บ๐๐๐บ๐๐ ๐ฒ๐๐๐๐พ ,\n> ๐ก๐บ๐๐๐บ๐๐๐ ๐ฃ๐บ๐๐พ๐ ๐ค๐๐๐พ ,\n> ๐ฒ๐พ๐๐๐ ๐ฒ๐๐๐ป๐พ๐ ๐ธ๐๐๐พ๐๐๐พ ,**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "๐ ๐ณ๐๐ ๐ช๐๐๐๐๐๐บ๐", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "๐ฏ๏ธ ๐ ๐๐บ ๐ฌ๐พ๐๐ ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "๐ฉ ๐๐พ๐๐พ๐๐๐๐พ๐", url="https://t.me/hurbeyy")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("โ **๐ญ๐๐ :\n\n ๐ก๐๐๐๐ ๐ ๐๐๐๐ฟ ๐ข๐บ๐๐๐๐๐บ๐๐ ๐๐ผ๐๐ ๐ฒ๐ ๐ด๐ผ ๐๐พ๐๐๐๐๐พ ๐๐๐๐๐๐บ๐ผ๐ ๐ต๐บ๐๐ฝ๐๐ :\n\n> ๐ฌ๐พ๐๐บ๐๐๐บ๐๐ ๐ฒ๐๐๐๐พ ,\n> ๐ก๐บ๐๐๐บ๐๐๐ ๐ฃ๐บ๐๐พ๐ ๐ค๐๐๐พ ,\n> ๐ฒ๐พ๐๐๐ ๐ฒ๐๐๐ป๐พ๐ ๐ธ๐๐๐พ๐๐๐พ ,**", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "๐ ๐ณ๐๐ ๐ช๐๐๐๐๐๐บ๐", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "๐ฏ๏ธ ๐ ๐๐บ ๐ฌ๐พ๐๐", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "๐ฉ ๐๐พ๐๐พ๐๐๐๐พ๐", url="https://t.me/hurbeyy")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nยป /vbul => แด ษชแดแดแด ษชษดแดษชส . \nยป /bul => แดแดแดขษชแด ษชษดแดษชส . \nยป /oynat => แดแดแดขษชแด แดสษดแดแด . \nยป /durdur => แดแดแดขษชษขษช แดแดสแดแดส . \nยป /devam => แดแดแดขษชษขษช sแดสแดแดส . \nยป /atla =>  แดแดแดขษชษขษช แดแดสแด . \nยป /son => แดแดแดขษชษขษช sแดษดสแดษดแดษชส . \nยป /katil => แดsษชsแดแดษดษช ษขสแดสแด แดแดแด แดแด แดแดแดส . \nยป /reload => แดแดแดษชษด สษชsแดแดsษชษดษช ษขแดษดแดแดสสแดส .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "๐ฉ ๐๐พ๐๐พ๐๐๐๐พ๐", url="https://t.me/hurbeyy")
                 ],
                 [
                     InlineKeyboardButton(
                         "โฌ๏ธ ๐ฆ๐พ๐๐ โฌ๏ธ", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler iรงin komut menรผsรผ ๐คฉ\n\n โถ๏ธ /devam - ลarkฤฑ รงalmaya devam et\n โธ๏ธ /durdur - รงalan parรงayฤฑ duraklatmak iรงin\n ๐ /atla- Sฤฑraya alฤฑnmฤฑล mรผzik parรงasฤฑnฤฑ atlatฤฑr.\n โน /son - mรผzik รงalmayฤฑ durdurma\n ๐ผ /ver botun sadece yรถnetici iรงin kullanฤฑlabilir olan komutlarฤฑnฤฑ kullanabilmesi iรงin kullanฤฑcฤฑya yetki ver\n ๐ฝ /al botun yรถnetici komutlarฤฑnฤฑ kullanabilen kullanฤฑcฤฑnฤฑn yetkisini al\n\n โช /asistan - Mรผzik asistanฤฑ grubunuza katฤฑlฤฑr.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "โ Geliลtirici", url="https://t.me/hurbeyy")
                 ],
                 [
                     InlineKeyboardButton(
                         "โฌ๏ธ Geri โฌ๏ธ", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""โ **๐ฌ๐พ๐๐๐บ๐ป๐บ** {query.from_user.mention} \n\nโ **๐ก๐พ๐** {bot} !\n\nโ **๐ฒ๐พ๐๐๐ ๐ฒ๐๐๐ป๐พ๐๐๐พ๐๐ฝ๐พ mรผzik ๐ข๐บ๐๐บ๐ป๐๐๐พ๐ ๐ก๐๐๐๐ . . !** \n\nโ **๐ก๐บ๐ ๐ธ๐พ๐๐๐๐๐๐, ๐ฒ๐พ๐ ๐ธ๐๐๐พ๐๐๐ ๐ธ๐พ๐๐๐๐๐ ๐๐พ๐๐๐ ๐ ๐๐๐๐๐บ๐๐ ๐ฆ๐๐๐ป๐บ ๐ค๐๐๐พ๐๐๐ . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ ๐๐๐ง๐ข ๐๐ซ๐ฎ๐๐ ๐๐ค๐ฅ๐ ๐", url=f"https://t.me/GlobalVideo_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐น๐ท ๐๐ฌ๐ข๐ฌ๐ญ๐๐ง", url="https://t.me/Globalvideo_bot"
                    ),
                    InlineKeyboardButton(
                        "๐ ๐๐๐ฌ๐ญ๐๐ค", url="https://t.me/hurbeyy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐จ๐ฆ๐ฎ๐ญ๐ฅ๐๐ซ" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "๐ ๐๐๐ง๐๐ฅ", url=f"https://t.me/ankara_sohbet_grubu"
                    )
                ]
                
           ]
        ),
    )
