import re

from parser.data_models import Article
from .telegram.config import TELEGRAM_MESSAGE_LENGTH_LIMIT


class Sender:
    def _get_message_for_send(self, article: Article, social_network: str) -> str:
        message_text_config = {
            'TELEGRAM': {
                'Bloomberg': '\n\n'.join(article.text[:2]),
                'Zerohedge': '\n\n'.join(article.text[:5])
            }
        }

        message_text = message_text_config[social_network][article.source]
        message_title = f'<b>{article.title}</b>\n\n'
        message_source = f'<b>{article.source}</b>\n\n'
        link_to_learn_more = '...\n<a href="https://www.facebook.com/SovereignWealthManagementLLC/">learn more</a>\n'
        message_hashtags = '  '.join(article.hashtags)

        message_text = f'{message_title}{message_text}{link_to_learn_more}{message_source}{message_hashtags}'
        return message_text

    def _get_divided_message(self, message_text: str, length_limit: int) -> list[str]:
        result_divided_message = []

        # код внизу разделяет сообщение на более мелкие части, 
        # если его длина больше максимальной длины в конкретной соц. сети, 
        # но если в конце части сообщения слово обрезалось не полностью, 
        # то оно удаляется из это части и переносится в начало message_text, 
        # который в свою очередь дальше продолжает разбиваться на части, 
        # если оно больше максимальной длины сообщения, в общем этот код обеспечивает, 
        # чтобы при разбивании сообщения на части оно разбивалось без переноса слов
        while len(message_text) > length_limit:
            message_part = message_text[:length_limit]
            message_end_regex = re.search(r'\s+\S+$', message_part)
            if message_end_regex:
                message_part = re.sub(fr'{message_end_regex.group(0)}$', '', message_part)
                message_text = message_end_regex.group(0) + message_text
            message_text = message_text[length_limit:]
            result_divided_message.append(message_part)

        if message_text:
            result_divided_message.append(message_text)
        return result_divided_message


            
