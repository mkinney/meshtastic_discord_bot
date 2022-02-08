#!/usr/bin/env python
"""help bot for Meshtastic discord group"""

import random
import asyncio
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")

discord_help_token = os.environ['DISCORD_HELP_TOKEN']

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    """eight ball simulator"""
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.event
async def on_ready():
    """on_ready"""
    game=Game(name="with humans")
    await client.change_presence(activity=game)
    print("Logged in as " + client.user.name)


async def list_servers():
    """list_servers"""
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(discord_help_token)
