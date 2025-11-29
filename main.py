import os

import discord
from discord.ext import commands
from discord import app_commands


bot = commands.Bot("!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.tree.command(name="echo", description="Echoes a message.")
@app_commands.describe(message="The message to echo.")
async def echo(interaction: discord.Interaction, message: str) -> None:
    await interaction.response.send_message(message)

bot.run(token=os.getenv("PRIZEPLAYER_TOKEN"))