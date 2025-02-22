from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("DISCORD_WEBHOOK_URL")

webhook = DiscordWebhook(url=url, content="Webhook Message")

response = webhook.execute()