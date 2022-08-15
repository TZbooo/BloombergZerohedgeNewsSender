import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = int(os.getenv('TELEGRAM_CHANNEL_ID'))
TELEGRAM_MESSAGE_LENGTH_LIMIT = 4095