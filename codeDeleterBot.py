import discord
from discord.ext import commands
import asyncio
import string
import re

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

_token = read_token()

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')
    game = discord.Game("Deleting your mistakes!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    #server_id = client.get_guild(755483080734539797)
    channels = ["codes"]
    match = re.search(r"\b[A-z!]{2}(\w{2}){1,2}\b", message.content)
    message_content = message.content
    error_message = "Looks like its not a Among Us code, try again!"


    if str(message.channel) in channels:
        if message.content == '!ping':
            await message.channel.send('@everyone')
        if(message.content == '!clear'):
             await message.channel.purge(limit=10)
        if message.attachments: 
            await message.channel.purge(limit=1)

        if not message_content.startswith("!"):
            if not message_content.startswith("@"):
                if not match:
                    if message.content != error_message:
                        await message.channel.purge(limit=1)
                        await message.channel.send(error_message)
                        await asyncio.sleep(3)
                        await message.channel.purge(limit=1)

        if message:
            await asyncio.sleep(300)
            try:
                await message.delete()
            except:
                print("oh-no")
        


client.run(_token)



