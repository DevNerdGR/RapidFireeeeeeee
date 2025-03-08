from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("DISCORD_WEBHOOK_URL")


def alertOnline():
    alertMessage("RapidFireeeeeeee Online! Type .start to being playing!")

def alertOffline():
    alertMessage("RapidFireeeeeeee is going offline :(")

def alertMessage(msg):
    webhook = DiscordWebhook(url=url, content=msg)
    response = webhook.execute()