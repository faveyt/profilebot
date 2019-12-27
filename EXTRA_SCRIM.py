import discord

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    game = discord.Game('구매 문의 Fave_-#9998')
    await client.change_presence(status=discord.Status.online, activity=game)

client.run('NjU4MDc0MzQzMjc1NzU3NTg5.Xf6dgg.F3n57p8ZUXbkWXJxx4omZz2dSwo')
