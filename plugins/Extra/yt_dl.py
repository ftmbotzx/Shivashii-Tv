# Don't Remove Credit @ftmdeveloperz
# Official Bot by Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ
# Ask Doubts on Telegram: @ftmdeveloperz

import os, requests, asyncio, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = f"[{user_name}](tg://user?id={user_id})"
    
    query = " ".join(message.command[1:])
    print(f"Searching: {query}")
    
    m = await message.reply(f"**🔍 Searching your song...!**\n**🎵 {query}**")
    
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "cookiesfrombrowser": ("chrome",)  # Change to "firefox" if needed
    }
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        
        thumb_name = f'thumb_{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        
        performer = "[Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ]"
        duration = results[0]["duration"]
        
    except Exception as e:
        print(f"Error: {e}")
        return await m.edit("❌ **Error:** Could not find the song.\nTry: `/song Believer`")
                
    await m.edit("**⬇️ Downloading your song...**")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        caption = "**🎧 Powered by [Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ](https://t.me/ftmdeveloperz)**"
        
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60

        await message.reply_audio(
            audio_file,
            caption=caption,            
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )            
        await m.delete()
        
    except Exception as e:
        await m.edit("❌ **Download Failed**\nPlease try again.")
        print(f"Download Error: {e}")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(f"Cleanup Error: {e}")


def get_text(message: Message) -> str:
    text = message.text
    if not text or " " not in text:
        return None
    return text.split(None, 1)[1]


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    query = get_text(message)
    m = await message.reply(f"**🔍 Searching for video:** `{query}`")
    
    if not query:
        return await m.edit("**Example:** `/video Shape of You`")     

    search = SearchVideos(query, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    
    try:
        url = mio[0]["link"]
        title = mio[0]["title"]
        video_id = mio[0]["id"]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        
    except Exception as e:
        print(f"Search Error: {e}")
        return await m.edit("❌ **Error:** Could not find the video.")

    await asyncio.sleep(0.6)
    wget.download(thumbnail_url, "thumb.jpg")

    ydl_opts = {
        "format": "best",
        "cookiesfrombrowser": ("chrome",),
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "quiet": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl_data = ydl.extract_info(url, download=True)
            
    except Exception as e:
        return await m.edit(f"❌ **Download Failed**\n**Error:** `{str(e)}`")

    video_file = f"{ydl_data['id']}.mp4"
    caption = f"**🎬 Title:** [{title}]({url})\n**🔗 Requested by:** {message.from_user.mention}"

    await client.send_video(
        message.chat.id,
        video=open(video_file, "rb"),
        duration=int(ydl_data["duration"]),
        file_name=str(ydl_data["title"]),
        thumb="thumb.jpg",
        caption=caption,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    
    await m.delete()
    
    for file in ("thumb.jpg", video_file):
        if file and os.path.exists(file):
            os.remove(file)# Don't Remove Credit @ftmdeveloperz
# Official Bot by Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ
# Ask Doubts on Telegram: @ftmdeveloperz

from __future__ import unicode_literals

import os, requests, asyncio, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = f"[{user_name}](tg://user?id={user_id})"
    
    query = " ".join(message.command[1:])
    print(f"Searching: {query}")
    
    m = await message.reply(f"**🔍 Searching your song...!**\n**🎵 {query}**")
    
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "cookiesfrombrowser": ("chrome",)  # Change to "firefox" if needed
    }
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        
        thumb_name = f'thumb_{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        
        performer = "[Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ]"
        duration = results[0]["duration"]
        
    except Exception as e:
        print(f"Error: {e}")
        return await m.edit("❌ **Error:** Could not find the song.\nTry: `/song Believer`")
                
    await m.edit("**⬇️ Downloading your song...**")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        caption = "**🎧 Powered by [Fᴛᴍ Dᴇᴠᴇʟᴏᴘᴇʀᴢ](https://t.me/ftmdeveloperz)**"
        
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60

        await message.reply_audio(
            audio_file,
            caption=caption,            
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )            
        await m.delete()
        
    except Exception as e:
        await m.edit("❌ **Download Failed**\nPlease try again.")
        print(f"Download Error: {e}")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(f"Cleanup Error: {e}")


def get_text(message: Message) -> str:
    text = message.text
    if not text or " " not in text:
        return None
    return text.split(None, 1)[1]


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    query = get_text(message)
    m = await message.reply(f"**🔍 Searching for video:** `{query}`")
    
    if not query:
        return await m.edit("**Example:** `/video Shape of You`")     

    search = SearchVideos(query, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    
    try:
        url = mio[0]["link"]
        title = mio[0]["title"]
        video_id = mio[0]["id"]
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        
    except Exception as e:
        print(f"Search Error: {e}")
        return await m.edit("❌ **Error:** Could not find the video.")

    await asyncio.sleep(0.6)
    wget.download(thumbnail_url, "thumb.jpg")

    ydl_opts = {
        "format": "best",
        "cookiesfrombrowser": ("chrome",),
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "quiet": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl_data = ydl.extract_info(url, download=True)
            
    except Exception as e:
        return await m.edit(f"❌ **Download Failed**\n**Error:** `{str(e)}`")

    video_file = f"{ydl_data['id']}.mp4"
    caption = f"**🎬 Title:** [{title}]({url})\n**🔗 Requested by:** {message.from_user.mention}"

    await client.send_video(
        message.chat.id,
        video=open(video_file, "rb"),
        duration=int(ydl_data["duration"]),
        file_name=str(ydl_data["title"]),
        thumb="thumb.jpg",
        caption=caption,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    
    await m.delete()
    
    for file in ("thumb.jpg", video_file):
        if file and os.path.exists(file):
            os.remove(file)
