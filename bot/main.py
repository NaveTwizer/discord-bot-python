from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member, User


import json



with open('./config/settings.json') as f:
    config = json.loads(f.read())
    f.close()

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")



@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx: Context, member: User = None, reason=None):
    if member == None or member == ctx.author:
        await ctx.channel.send("You must mention a user, someone that isn't you.")
        return
    if reason is None:
        reason = f"Reason not provided.\nBanned by {ctx.author}"

    message = (f"You have been banned from **{ctx.guild.name}**. Reason:\n**{reason}**")
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} was banned due to **{reason}**")


if __name__ == "__main__":
    bot.run(config["token"])