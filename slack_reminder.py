import os
import schedule
import time
from slack_sdk import WebClient

# Load Slack token and channel ID from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

if not SLACK_BOT_TOKEN or not SLACK_CHANNEL_ID:
    raise ValueError("Slack token or channel ID not set in environment variables!")

client = WebClient(token=SLACK_BOT_TOKEN)

def send_reminder():
    try:
        client.chat_postMessage(
            channel=SLACK_CHANNEL_ID,
            text=" 8 PM Reminder!\nGitHub ma `git pull` ra `git push` garna nabirsinu"
        )
        print("Reminder sent!")
    except Exception as e:
        print("Failed to send reminder:", e)

# Schedule the reminder at 8 PM every day
schedule.every().day.at("20:00").do(send_reminder)

print("Slack reminder bot is running... Waiting for 8 PM.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
