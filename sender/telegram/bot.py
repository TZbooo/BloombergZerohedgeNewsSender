import re

from telebot import TeleBot

from parser.data_models import Article, SocialNetwork
from sender.sender import Sender


class TelegramSender(Sender):
    def __init__(self, bot_token: str, channel_id: int) -> None:
        self.__bot = TeleBot(bot_token, parse_mode='html')
        self.__channel_id = channel_id

    def send_article(self, article: Article) -> None:
        message_text = self._get_message_for_send(article, SocialNetwork.TELEGRAM)
        self.__bot.send_message(
            chat_id=self.__channel_id,
            text=message_text,
        )
