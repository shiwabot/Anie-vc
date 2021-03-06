

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

@Client.on_message(filters.command("song") & ~filters.edited)
async def song(client, message):
    cap = "@JEBotZ"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("ꜰɪɴᴅɪɴɢ ...")
    if not url:
        await rkp.edit("**ᴛʏᴘᴇ ꜱᴏᴍᴇᴛʜɪɴɢ ᴡʜᴀᴛ ᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ **\nUsage`/song <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("ᴜᴘʟᴏᴀᴅ ʙʏ {BOT_USERNAME}")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("ꜰɪɴᴅɪɴɢ ...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`ꜰɪɴᴅɪɴɢ ᴇʀʀᴏʀꜱ ꜱᴏᴍᴇᴛʜɪɴɢ`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ @Zaid2_Robot`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`ᴛᴏᴏ ᴍᴀɴʏ ʀᴇQᴜᴇꜱᴛꜱ`")
        return
    except PostProcessingError:
        await rkp.edit("`something went wrong `")
        return
    except UnavailableVideoError:
        await rkp.edit("`ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ।`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("ᴅᴏɴᴇ...") #ImJanindu
        lol = "./etc/thumb.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)  #JEBotZ
        await rkp.delete()
