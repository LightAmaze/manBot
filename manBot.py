import discord
import sys
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        await client.send_message(message.channel, message.author.mention+", hey!")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(sys.argv[1])