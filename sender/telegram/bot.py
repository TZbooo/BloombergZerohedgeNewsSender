import json
import hashlib

from telebot import TeleBot

from parser.data_models import Article, SocialNetwork
from sender.sender import Sender


class TelegramSender(Sender):
    def __init__(self, bot_token: str, channel_id: int) -> None:
        self.__bot = TeleBot(bot_token, parse_mode='html')
        self.__channel_id = channel_id

    def send_article(self, article: Article) -> None:
        message_text = self._get_message_for_send(
            article, SocialNetwork.TELEGRAM)

        with open('auto-sender-cache.json', 'r', encoding='utf-8') as file:
            auto_sender_cache = json.load(file)

        if hashlib.md5(article.title.encode('utf-8')).hexdigest() == auto_sender_cache[article.source]['last_article_title_hash']:
            return False
        auto_sender_cache[article.source]['last_article_title_hash'] = hashlib.md5(article.title.encode('utf-8')).hexdigest()

        with open('auto-sender-cache.json', 'w', encoding='utf-8') as file:
            json.dump(auto_sender_cache, file, indent=4)

        self.__bot.send_message(
            chat_id=self.__channel_id,
            text=message_text,
        )
