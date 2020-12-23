import discord

from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self):
        ...

    @commands.command(name='create-channel')
    @commands.has_role('Administrators')
    async def create_channel(ctx, channel_name='real-python'):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)