#!/usr/bin/env python
"""help bot for Meshtastic discord group"""

import random
import asyncio
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")

discord_help_token = os.environ['HELP_BOT_TOKEN']

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
async def on_message(message):

    # Do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!gs'):
        msg = 'https://meshtastic.org/docs/getting-started'
        await message.channel.send(msg)
        # get the user's requested message and delete it
        await message.delete()

    if message.content.startswith('!esp'):
        msg = 'https://meshtastic.org/docs/getting-started/flashing-esp32'
        await message.channel.send(msg)
        await message.delete()

    if message.content.startswith('!nrf'):
        msg = 'https://meshtastic.org/docs/getting-started/flashing-nrf52'
        await message.channel.send(msg)
        await message.delete()

    if message.content.startswith('!ant'):
        msg = 'https://meshtastic.org/docs/hardware/antenna'
        await message.channel.send(msg)
        await message.delete()

    if message.content.startswith('!help'):
        msg = '''
!hello - replies with 'hello <username>'
!help - this page
!esp - show esp flashing page
!nrf - show nrf flashing page
!ant - show antenna page
'''
        await message.channel.send(msg)


@client.event
async def on_ready():
    """on_ready"""
    game=Game(name="with humans")
    await client.change_presence(activity=game)
    print("Logged in as " + client.user.name)


client.run(discord_help_token)
