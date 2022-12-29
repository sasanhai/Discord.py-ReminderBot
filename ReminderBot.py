import random
import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    channels = {
        '1057663256761737306': {
            'messages': ['Hello!', 'How are you?', 'What is your favorite color?', 'Do you like to code?'],
            'delay': (10, 20)  # Minimum and maximum delay in seconds
        },
        '1057663286272856216': {
            'messages': ['Hi there!', 'What do you like to do in your free time?', 'Do you have any pets?'],
            'delay': (10, 20)  # Minimum and maximum delay in seconds
        },
        '1057663337581776936': {
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

client.run('OTQyODE0MDQ3MzUzNTk3OTUy.GZuPeC.Ezt55wTVoVUI3I_OsbgID_ozRaSHBZhFVZ_Y78')
#The purpose of this code is to create a Discord bot that sends random messages to specific channels at regular intervals. The bot selects a random message from a list of messages for each channel and sends it to the channel, then waits for a random delay before sending the next message. This allows the bot to send a variety of messages to each channel and helps to keep the conversation lively and engaging.

#To use this code, you will need to create a Discord bot and get its token. You can find instructions on how to do this in the Discord developer documentation. Once you have your bot's token, you can replace the YOUR_BOT_TOKEN_HERE placeholder in the code with your bot's token.

#You can also customize the messages and delays for each channel by modifying the channels dictionary in the code. To add a new message for a channel, you can simply add it to the appropriate list in the dictionary. To change the delay for a channel, you can modify the delay tuple in the dictionary.