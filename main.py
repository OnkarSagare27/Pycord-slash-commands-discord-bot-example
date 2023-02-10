import discord
from discord.commands import SlashCommandGroup, option
from discord.ext import commands
import json
import traceback

file = open("config.json", "r", encoding="utf-8")
configData = json.load(file)

if __name__ == "__main__":
    intents= discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix=commands.when_mentioned,
                       sync_commands_debug=True, intents=intents)
    
    initial_extensions = [
        "commands.testcommandone"
    ]

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as extension:
            traceback.print_exc()

    bot.run(configData["token"])