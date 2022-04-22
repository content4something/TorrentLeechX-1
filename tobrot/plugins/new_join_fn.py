#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>🙋🏻‍♂️ Hello dear!\n\n This Is A Leech Bot .This Chat Is Not Supposed To Use Me</b>\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Github', url='https://github.com/AmirulAndalib')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    if UPLOAD_AS_DOC:
        utxt = "Document"
    else:
        utxt = "Streamable"
    await message.reply_text(
        """<i>▼This is the list of CMDS available for the bot.▼\n\n/gclone - This command is used to clone gdrive files or folder using gclone.\n\n/ytdl - This command should be used as reply to a supported link.\n\n/pytdl - This command will download videos from youtube playlist link and will upload to telegram.\n\n/gytdl - This will download and upload to your cloud.\n\n/gpytdl - This download youtube playlist and upload to your cloud.\n\n/leech - leech any torrent/magnet/direct-download link to Telegram.\n\n/leecharchive - leech any torrent/magnet/direct-download link to Telegram and Upload It as .tar.gz acrhive...\n\n/gleech - leech any torrent/magnet/direct-download link to cloud.\n\n/garchive - leech any torrent/magnet/direct-download link to Cloud and Upload It as .tar.gz acrhive...\n\n/leechextract - This will unarchive file and upload to telegram.\n\n/gextract - This will unarchive file and upload to cloud.\n\n/tleech - This will mirror the telegram files to ur respective cloud.\n\n/tleechextract - This will unarchive telegram file and upload to cloud.\n\n/savethumb - To Add Thumbnail To File.\n\n/clearthumb - To Remove Previously Added Thumbnail.\n\n/status - show status of current downloads and stuff.\n\n/getsize - This will give you total size of your destination folder in cloud.\n\n/rename - you can do rename to files.\n\n/toggledoc - choose whether the file shall be uploaded as doc or not.\n\n/togglevid - choose whether the file shall be uploaded as streamable or not.\n\n/help - send help.\n\n/tshelp - get help for torrent search module.\n\n/speedtest - check speedtest of the host.\n\n/renewme - clear all downloads.(admin only)⚠️\n\n/log - This will send you a txt file of the logs.(admin only)⚠️\n\n/rclone - This will change your drive config on fly.(First one will be default)--(admin only)⚠️</i>""",
        disable_web_page_preview=True,
    )
