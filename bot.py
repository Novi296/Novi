import discord
import random
import json
import os
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix = '/')
os.chdir(r'PATH TO YOUR DISCORD BOT FILE')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
     await member.kick(reason=reason)
     await ctx.send(f'{member.mention} wurde gekickt ')@client.command(pass_context=True)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member):
    if ctx.author.guild_permissions.ban_members:
            await member.ban()
            await ctx.send(f'{member.mention} wurde gebannt!')


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} wurde entbannt')
            return 

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_ready():
    activity = discord.Game(name="Programmiert von Novi#0187", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")






client.run ('TOKEN')