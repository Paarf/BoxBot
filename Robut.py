import discord
import logging
import time
import datetime
import youtube_dl
from discord.ext import commands
from settings import token

logging.basicConfig(level=logging.INFO)

startuptime = int(time.time())


class YoutubeSource(discord.FFmpegPCMAudio):
    def __init__(self, url):
        opts = {
            'format': 'webm[abr>0]/bestaudio/best',
            'prefer_ffmpeg': True,
            'quiet': True
        }
        ytdl = youtube_dl.YoutubeDL(opts)
        info = ytdl.extract_info(url, download=False)
        super().__init__(info['url'])


class MyClient(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        extensions = ["cogs"]
        # extensions could be:
        # extensions = ["cogs.bla", "cogs.boop", "myfile"]
        for ext in extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f"{ext} could not be loaded: {e.__class__.__name__}: {e}")

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # with open("avatar.png", "rb") as f:
        #     avatar = f.read()
        # await client.user.edit(username="BoxBot", avatar=avatar)
        # this is also not nessessary, just eats internet each time you start with that photo

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(f"{self.user.mention} uptime"):
            uptime = int(time.time()) - startuptime
            divider = 60
            uptime = divmod(uptime % divider)
            await message.channel.send(uptime)

        if message.content.startswith(f"{self.user.mention} play "):
            message2 = message.content.replace(f"{self.user.mention} play ", "")
            source = YoutubeSource(message2)
            voice_client = await client.get_channel(264541926378831872).connect()
            voice_client.play(source)

        await self.process_commands(message)




client = MyClient(command_prefix=commands.when_mentioned, game=discord.Game(name='Currently under development'))
client.run(token)
