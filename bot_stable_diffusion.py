import discord
from discord.ext import commands

TOKEN = 'Discord Bot Token'
intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='.', intents=intents)




@client.event
async def on_ready():
    print('I am ready to get weird Daddy OwO')
    
# @client.event
# async def on_message(message):
#     #channel = client.get_channel(1030698526075785298)
#     #await channel.send('testing')
#     print(message.author, message.content, message.channel.id)
# #     pass


@client.command()
async def hello(ctx):
    channel = client.get_channel(channelID)
    await channel.send(f'hello there {ctx.author.mention}')
    
    
client.run(TOKEN)
