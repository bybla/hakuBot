import json
import disnake
from disnake.ext import commands 

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='s.', intents=intents) 
bot.remove_command("help")

with open('config.json') as f:
    data = json.load(f)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.load_extension("cogs.vacancy")

bot.run(f"{data["token"]}")