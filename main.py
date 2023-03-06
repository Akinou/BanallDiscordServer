import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command()
async def remove_all_members(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban(reason="Removing all members")
        except:
            pass
    await ctx.send("All members have been removed from the server")

client.run('YOUR_DISCORD_BOT_TOKEN')
