import discord
from discord.commands import SlashCommandGroup, option, slash_command
from discord.ext import commands
import traceback

class TestCommancOne(commands.Cog):

    """
    A normal slash command example which takes discord member as a command parameter
    ----------
    /testcommandone <user>
    """

    def __init__(self, bot_: discord.Bot):
        self.bot = bot_

    @commands.slash_command(description="A normal slash command example which takes discord member as a command parameter", guild_only=True)
    @option("member", description="Select member or enter member id")
    async def testcommandone(self, ctx: discord.ApplicationContext, member: discord.Member):
        await ctx.respond(f"{ctx.interaction.user.mention} Hello! this is a test command with a member as a paramater i.e {member.mention}")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, commands.NotFound):
            await ctx.respond("Not found error triggered.")
        else:
            raise error

def setup(bot):
    bot.add_cog(TestCommancOne(bot))
