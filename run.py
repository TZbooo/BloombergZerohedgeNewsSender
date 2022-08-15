import time

import schedule

from parser.zerohedge.zerohedge_parser import ZeroHedgeParser
from parser.bloomberg.bloomberg_parser import BloombergParser
from parser.config import ZEROHEDGE_ARTICLES_PAGE_URL, BLOOMBERG_ARTICLES_PAGE_URL
from sender.telegram.bot import TelegramSender
from sender.telegram.config import TELEGRAM_CHANNEL_ID, TELEGRAM_BOT_TOKEN


def send_articles():
    zerohedge_parser = ZeroHedgeParser(ZEROHEDGE_ARTICLES_PAGE_URL)
    bloomberg_parser = BloombergParser(BLOOMBERG_ARTICLES_PAGE_URL)
    zerohedge_article = zerohedge_parser.get_latest_article()
    bloomberg_article = bloomberg_parser.get_latest_article()
    telegram_sender = TelegramSender(TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID)
    telegram_sender.send_article(zerohedge_article)
    telegram_sender.send_article(bloomberg_article)


if __name__ == '__main__':
    schedule.every().day.at('10:48').do(send_articles)

    while True:
        schedule.run_pending()
        time.sleep(1)