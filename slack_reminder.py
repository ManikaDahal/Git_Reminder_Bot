import os
from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")  

if not SLACK_BOT_TOKEN or not CHANNEL_ID:
    raise ValueError("Slack token or channel ID not set in environment variables!")

client = WebClient(token=SLACK_BOT_TOKEN)

client.chat_postMessage(
    channel=CHANNEL_ID,
    text=" 8 PM Reminder!\nGitHub ma `git pull,push` garna nabirsinu"
)
