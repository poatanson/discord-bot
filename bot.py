import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

DISCORD_BOT_KEY = 'MTM0OTM0MDgxNTIwNTMzOTE0Ng.GsV_V1.sXeQ35gagQNFe210sE_pHaPFva2UNRBmdtDZqQ'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_BOT_KEY)