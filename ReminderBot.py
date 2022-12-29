import random
import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('..OK !')
    print(client.user.name)
    print(client.user.id)
    print('BOT IS NOW ON')

    channels = {
        'channel_1': {
            'messages': ['Hello!', 'How are you?', 'What is your favorite color?', 'Do you like to code?'],
            'delay': (10, 20)  # Minimum and maximum delay in seconds
        },
        'channel_2': {
            'messages': ['Hi there!', 'What do you like to do in your free time?', 'Do you have any pets?'],
            'delay': (10, 20)  # Minimum and maximum delay in seconds
        },
        'channel_3': {
            'messages': ['Good morning!', 'What did you have for breakfast?', 'Do you have any hobbies?'],
            'delay': (3, 5)  # Minimum and maximum delay in seconds
        }
    }
    while True:
        for channel_id, channel_data in channels.items():    
            channel = client.get_channel(int(channel_id))
            message = random.choice(channel_data['messages']) if channel_data['messages'] else 'No messages available'
            await channel.send(message)
            await asyncio.sleep(random.randint(*channel_data['delay']))

client.run('YOUR_BOT_TOKEN_HERE')
