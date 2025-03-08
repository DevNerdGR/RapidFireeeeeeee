from dotenv import load_dotenv
import os
from discord.ext.commands import Bot
import discord
import questionRetriever
from questionRetriever import QuestionCategory
import main
import discordWebhookInterface
import signal

helpBanner = f"""
# RapidFireeeeeeee: Rapid Response Training Bot, v{main.getVersionNumber()}
## Created by Tew Gun Rui
### Usage:
Type ".<command>" into the chat box and send it! The bot will respond with the appropriate output.
E.g. To start the game, simply type ".start" and send the message.
### Commands:
- ```.hi : show information about the bot```
- ```.start : start the bot```
- ```.guess <guess> : submit a guess to the bot (note: replace <guess> with your answer to the question)```
- ```.skip : skip the current question and show the correct answer```
- ```.commands : show this help page!```
"""

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = Bot(command_prefix=".", intents=intents, help_command=None)
bot.remove_command("help")

qnGen = questionRetriever.QuestionGenerator()

answer = ""

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for g in bot.guilds:
        print(g.name)
    discordWebhookInterface.alertOnline()

@bot.command(name="hi")
async def onGreeting(ctx, *args):
    await ctx.message.channel.send("Hi! 🔥 \nNeed help? Type the command .commands to see all available commands!")

@bot.command(name='guess')
async def onGuess(ctx, *args):
    print(len(args))
    if len(args) != 1:
        await ctx.message.channel.send("Invalid input! Please enter exactly one word as your answer.")
    else:
        if args[0].lower().strip() == answer.lower().strip():
            await ctx.message.channel.send("Correct! Next question")
            await sendQuestion(ctx)
        else:
            await ctx.message.channel.send("Wrong, try again or skip with command .skip")

@bot.command(name="start")
async def sendQuestion(ctx, *args):
    qn = qnGen.getQuestion(QuestionCategory.randomCategory())
    global answer
    answer = qn.answer
    await ctx.message.channel.send(f"Question: {qn.question}")

@bot.command(name="skip")
async def onSkip(ctx, *args):
    await ctx.message.channel.send(f"Question skipped! The answer was \"{answer}\"")
    await sendQuestion(ctx)

@bot.command(name="commands")
async def onHelp(ctx, *args):
    await ctx.message.channel.send(helpBanner)

def exitHandler(signum, frame):
    discordWebhookInterface.alertOffline()
    exit(0)

signal.signal(signal.SIGINT, exitHandler)

def startBot():
    bot.run(TOKEN)