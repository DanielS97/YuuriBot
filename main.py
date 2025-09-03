import os
import discord
import random
from discord.ext import commands

bot_token = os.environ.get("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

gif_url = "https://cdn.discordapp.com/attachments/819429350986350612/1412150288227373176/wtfweyl.gif?ex=68b93931&is=68b7e7b1&hm=1e8edbafb25e8f1c4b2974c4eae7a00c6a646a89021717439c49b43a94eb4ded"


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "weyl" in message.content.lower():
        if random.random() < 0.6:
            await message.channel.send(gif_url)

    await bot.process_commands(message)

bot.run(bot_token)
