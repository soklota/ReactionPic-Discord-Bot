import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
GUILD_ID = discord.Object(id=1529995986770989278)  # paste your actual number, no quotes

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # needed if your bot reads message text
bot = commands.Bot(command_prefix="!", intents=intents) 


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.tree.copy_global_to(guild=GUILD_ID)
    synced = await bot.tree.sync(guild=GUILD_ID)
    print(f"Synced {len(synced)} command(s) to guild")

#/ping command will respond with "Pong!" when used in Discord chat
@bot.tree.command(name="ping", description="Replies with Pong!")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.command()  # old style, triggered by !ping
async def ping(ctx):
    await ctx.send("Pong!")

@bot.tree.command(name="sad", description="Replies with a random Sad Image") 
async def slash_sad(interaction: discord.Interaction):
    await interaction.response.send_message("Here's a sad image!")

bot.run(TOKEN)