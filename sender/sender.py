import re

from parser.data_models import Article


class Sender:
    def _get_message_for_send(self, article: Article, social_network: str) -> str:
        message_text = '\n\n'.join(article.text)
        message_title = f'<b>{article.title}</b>\n\n'
        message_source = f'<b>{article.source}</b>\n\n'
        link_to_learn_more = '...\n<a href="https://www.facebook.com/SovereignWealthManagementLLC/">learn more</a>\n'
        message_hashtags = '  '.join(article.hashtags)

        if social_network == 'TELEGRAM':
            message_text = message_text[:4095 - len(message_title) - len(message_source) - len(message_hashtags) - len(link_to_learn_more)]
            message_end_regex = re.search(r'\s+\S*$', message_text)
            if message_end_regex:
                message_text = re.sub(fr'{message_end_regex.group(0)}$', '', message_text)
        message_text = f'{message_title}{message_text}{link_to_learn_more}{message_source}{message_hashtags}'

        return message_text

    def _get_divided_message(self, message_text: str, length_limit: int) -> list[str]:
        result_divided_message = []
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


            