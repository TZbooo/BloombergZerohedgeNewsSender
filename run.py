import time
import os

import schedule
from xvfbwrapper import Xvfb

from parser.zerohedge.zerohedge_parser import ZeroHedgeParser
from parser.bloomberg.bloomberg_parser import BloombergParser
from parser.config import ZEROHEDGE_ARTICLES_PAGE_URL, BLOOMBERG_ARTICLES_PAGE_URL
from sender.telegram.bot import TelegramSender
from sender.telegram.config import TELEGRAM_CHANNEL_ID, TELEGRAM_BOT_TOKEN
from logger import logger


def send_articles():
    with Xvfb() as xvfb:
        logger.info('start init parsers')
        zerohedge_parser = ZeroHedgeParser(ZEROHEDGE_ARTICLES_PAGE_URL, False)
        logger.info('zerohedge parser init')
        bloomberg_parser = BloombergParser(BLOOMBERG_ARTICLES_PAGE_URL, False)
        logger.info('bloomberg parser init')
        logger.info('start parsing')
        zerohedge_article = zerohedge_parser.get_latest_article()
        bloomberg_article = bloomberg_parser.get_latest_article()
        logger.info('end parsing')
        logger.info('start sending')
        telegram_sender = TelegramSender(TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID)
        telegram_sender.send_article(zerohedge_article)
        telegram_sender.send_article(bloomberg_article)
        logger.info('end sending')


if __name__ == '__main__':
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    schedule.every().day.at('18:25').do(send_articles)

    while True:
        schedule.run_pending()
        time.sleep(1)
