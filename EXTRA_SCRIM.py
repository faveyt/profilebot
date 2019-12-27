import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    game = discord.Game('구매 문의 Fave_-#9998')
    await client.change_presence(status=discord.Status.online, activity=game)
    
access_token = os.environ["BOT_TOKEN"]    
client.run(access_token)
