import re

from parser.data_models import Article


class Sender:
    def _get_message_for_send(self, article: Article, social_network: str) -> str:
        message_text_config = {
            'TELEGRAM': {
                'Bloomberg': '\n\n'.join(article.text[:2]),    # get 2 first paragraphs
                'Zerohedge': '\n\n'.join(article.text[:5]),    # get 5 first paragraphs
            },
            'FACEBOOK': {
                'Bloomberg': '\n\n'.join(article.text),
                'Zerohedge': '\n\n'.join(article.text),
            },
        }

        message_text = message_text_config[social_network][article.source]
        message_title = article.title + '\n\n'
        message_source = article.source
        link_to_learn_more = '...\n<a href="https://www.facebook.com/SovereignWealthManagementLLC/">learn more</a>\n'

        if social_network == 'FACEBOOK':
            link_to_learn_more = ''

        message_hashtags = '  '.join(article.hashtags)

        message_text = f'{message_title}{message_text}{link_to_learn_more}\n\n{message_source}\n\n{message_hashtags}'
        return message_text
