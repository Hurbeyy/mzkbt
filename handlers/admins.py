from asyncio.queues import QueueEmpty
from cache.admins import admins
from asyncio import sleep
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
from pyrogram import filters

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command(["durdur"]) & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    a = await message.reply_text("▶️ **𝐌𝐮𝐳𝐢𝐤 𝐃𝐮𝐫𝐝𝐮𝐫𝐮𝐥𝐝𝐮 !**\n\n• **𝐂𝐚𝐥𝐦𝐚𝐲𝐚 𝐃𝐞𝐯𝐚𝐦 𝐄𝐭𝐦𝐞𝐤 𝐢𝐜𝐢𝐧\n /devam 𝐊𝐨𝐦𝐮𝐭𝐮𝐧𝐮 𝐊𝐮𝐥𝐥𝐚𝐧𝐢𝐧 !**")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["devam"]) & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    a = await message.reply_text("⏸ **𝐌𝐮𝐳𝐢𝐤 𝐃𝐞𝐯𝐚𝐦 𝐄𝐝𝐢𝐲𝐨𝐫 !**\n\n• **𝐃𝐮𝐫𝐝𝐮𝐫𝐦𝐚𝐤 𝐢𝐜𝐢𝐧 /durdur 𝐊𝐨𝐦𝐮𝐭𝐮𝐧𝐮 𝐊𝐮𝐥𝐥𝐚𝐧𝐢𝐧 !**")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["son"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = message.chat.id 
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("• **𝐒𝐮 𝐀𝐧𝐝𝐚 𝐌𝐮𝐳𝐢𝐤 𝐂𝐚𝐥𝐦𝐢𝐲𝐨𝐫 !**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "✅ **𝐌𝐮𝐳𝐢𝐤 𝐒𝐨𝐧𝐥𝐚𝐧𝐝𝐢𝐫𝐢𝐥𝐝𝐢 !**\n\n• **𝐒𝐞𝐬𝐥𝐢 𝐒𝐨𝐡𝐛𝐞𝐭𝐭𝐞𝐧 𝐀𝐲𝐫𝐢𝐥𝐢𝐲𝐨𝐫𝐮𝐦 !**"
        )
    
@Client.on_message(command(["atla"]) & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        a = await message.reply_text("• **𝐒𝐞𝐬𝐥𝐢 𝐒𝐨𝐡𝐛𝐞𝐭𝐭𝐞 𝐌𝐮𝐳𝐢𝐤 𝐘𝐨𝐤 !**")
        await sleep(3)
        await a.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
            
        a = await message.reply_text("➡️ **𝐒𝐚𝐫𝐤𝐢 𝐀𝐭𝐥𝐚𝐭𝐢𝐥𝐝𝐢 . . .**")
        await sleep(3)
        await a.delete()

# Yetki Vermek için (ver) Yetki almak için (al) komutlarını ekledim.
# Gayet güzel çalışıyor. @Mahoaga Tarafından Eklenmiştir. 
@Client.on_message(command("ver") & other_filters)
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Kullanıcıya Yetki Vermek için yanıtlayınız!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkili.")
    else:
        await message.reply("✔ Kullanıcı Zaten Yetkili!")


@Client.on_message(command("al") & other_filters)
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✅ Kullanıcıyı yetkisizleştirmek için mesaj atınız!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkisiz")
    else:
        await message.reply("✅ Kullanıcının yetkisi alındı!")


# Sesli sohbet için 0-200 arası yeni komut eklenmiş oldu. 
@Client.on_message(command(["ses"]) & other_filters)
@authorized_users_only
async def change_ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **Birim olarak ayarlandı:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**hata:** {e}")

@Client.on_message(command("reload") & other_filters)
@errors
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await client.send_message(
        message.chat.id,
        "✅ **𝐁𝐨𝐭 𝐘𝐞𝐧𝐢𝐝𝐞𝐧 𝐁𝐚𝐬𝐥𝐚𝐭𝐢𝐥𝐝𝐢 !**\n✅ **𝐀𝐝𝐦𝐢𝐧 𝐋𝐢𝐬𝐭𝐞𝐬𝐢 𝐆𝐮𝐧𝐜𝐞𝐥𝐥𝐞𝐧𝐝𝐢 !**"
    )
