import discord
import random
from token import *

TOKEN = '#############################################'

client = discord.Client()

@client.event
async def on_ready():
    print('Estamos logados como {0.user}'.format(client))

#funções de mensagem
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'memorial-hall' or message.channel.name == 'management':
        if user_message.lower() == 'oi':
            await message.channel.send(f'Olá {username}')
            return
        elif user_message.lower() == 'flw':
            await message.channel.send(f'Até a próxima {username}')
            return
        elif user_message.lower() == '!random':
            response = f'O random é você, seu número aleatório é: {random.randrange(10000000)}'
            await message.channel.send(response)
            return
        
client.run(TOKEN)





