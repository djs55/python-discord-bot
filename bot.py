#!/usr/bin/env/python

# From https://medium.com/@moomooptas/how-to-make-a-simple-discord-bot-in-python-40ed991468b4

import discord, os

print("Bot started")

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    # The bot should never respond to itself, or it might get into a loop
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

# The token must never be added to the source code, otherwise other people would be able to steal it.
if "DISCORD_BOT_TOKEN" not in os.environ:
    print("You must set the environment variable DISCORD_BOT_TOKEN.")
else:
    client.run(os.environ["DISCORD_BOT_TOKEN"])