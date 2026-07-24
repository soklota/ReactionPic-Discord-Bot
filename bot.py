import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
GUILD_ID = discord.Object(id=1529995986770989278)  # paste your actual number, no quotes

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

sad_images = ["images/sad_imgs/crying.jpg"]  #sad images
tea_images = ["images/tea_imgs/tea1.jpg", "images/tea_imgs/tea2.jpg", "images/tea_imgs/tea3.jpg", "images/tea_imgs/tea4.jpg"]  #tea images
intents = discord.Intents.default()
intents.message_content = True  # needed if your bot reads message text
bot = commands.Bot(command_prefix="!", intents=intents) 


@bot.event #guild only sync
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.tree.copy_global_to(guild=GUILD_ID)
    synced = await bot.tree.sync(guild=GUILD_ID)
    print(f"Synced {len(synced)} command(s) to guild")

@bot.event #global sync
async def on_ready():
    print(f"Logged in as {bot.user}")
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s) globally")

#/ping command will respond with "Pong!" when used in Discord chat
@bot.tree.command(name="ping", description="Replies with Pong!")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.command()  # old style, triggered by !ping
async def ping(ctx):
    await ctx.send("Pong!")

#slash commands
@bot.tree.command(name="sad", description="Replies with a random Sad Image") 
async def slash_sad(interaction: discord.Interaction):
    await interaction.response.send_message("sobbing...")  # send an initial response to acknowledge the command
    random_img = random.choice(sad_images)  # make sure crying.jpg is in the same directory
    await interaction.followup.send(file=discord.File(random_img))

@bot.tree.command(name="tea", description="Replies with a random Tea Image")
async def slash_tea(interaction: discord.Interaction):
    await interaction.response.send_message("OOoooOOo TEA!")  # send an initial response to acknowledge the command
    random_img = random.choice(tea_images)  # make sure one of the tea images is in the same directory
    await interaction.followup.send(file=discord.File(random_img))

bot.run(TOKEN)