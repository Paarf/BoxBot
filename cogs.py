# -*- coding: utf-8 -*-
import discord
from discord.ext import commands


class Commands:
    def __init__(self, bot):
        self.bot = bot

    # you can use events here too
    async def on_message(self, msg):
        print(msg.content)

    # or commands like this
    @commands.command()
    async def a(self, ctx):
        await ctx.send("b")

    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f"hello {ctx.author.mention} <:301100937659809792:318009894579994624>")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{ctx.author.mention}")

    @commands.command()
    async def length(self,ctx):
        await ctx.send(f"The message length is {len(ctx.message.content) - 29}")

    @commands.command()
    async def info(self,ctx, member : discord.Member = None):
        if member is None:
            member = ctx.message.author

        embed = discord.Embed(title="User Info", colour=member.colour,description="General info about a Discord Account")
        embed.set_image(url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=str(member), url="https://discordapp.com", icon_url=member.avatar_url)
        embed.set_footer(text=discord.Guild.name, icon_url=member.avatar_url)
        embed.add_field(name="Nitro Account", value="TBD")
        embed.add_field(name="Bot Account", value="test")
        embed.add_field(name="Displayed Name", value=str(member))
        embed.add_field(name="<:thonkang:325666093161250816>", value="these last two", inline=True)
        embed.add_field(name="<:thonkang:325666093161250816>", value="are inline fields", inline=True)

        await ctx.send(content="User Info", embed=embed)




def setup(bot):
    bot.add_cog(Commands(bot))
