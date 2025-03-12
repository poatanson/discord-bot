import discord
import os 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name="ping", description="Sends the bot's latency.")
async def ping(ctx: discord.ApplicationContext): 
    await ctx.respond(f"Pong! Latency is {bot.latency}")

bot.run(os.getenv('TOKEN')) # run the bot with the token