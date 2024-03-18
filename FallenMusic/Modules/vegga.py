import asyncio

import os
import time
import requests
from config import START_IMG
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from FallenMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين تيتو","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cde2b51203fbdab57fac5.jpg",
        caption=f"""**⩹━★⊷⌯᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين تيتو ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷⌯᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "˹ ᴏɢ ✗ ᴛᴇᴛᴏ ˼", url=f"https://t.me/WZAERE"), 
                 ],[
                    InlineKeyboardButton(
                        "᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆", url=f"https://t.me/WX_PM"),
                ],[
                    InlineKeyboardButton(
                        "ხ᥆ƚᥲƚƚᎥ", url=f"https://t.me/T_S_T4"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["تيتو"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("WX_PM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷⌯᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆⌯⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷⌯᥉᥆ᥙᖇᥴᥱ ƚᥱƚ᥆⌯⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
    
   



