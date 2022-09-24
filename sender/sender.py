import os
import json
import hashlib

from logger import logger
from parser.data_models import Article


class Sender:
    def _get_message_for_send(self, article: Article, social_network: str) -> str:
        message_text_config = {
            'TELEGRAM': {
                # get 2 first paragraphs
                'bloomberg.com': '\n\n'.join(article.text[:2]),
                # get 5 first paragraphs
                'zerohedge.com': '\n\n'.join(article.text[:5]),
            }
        }

        message_text = message_text_config[social_network][article.source]
        link_to_learn_more = '...\n<a href="https://www.facebook.com/SovereignWealthManagementLLC/">learn more</a>\n'

        message_text = (f'{article.title}\n\n'
                        f'{message_text}'
                        f'{link_to_learn_more}\n\n'
                        f'{article.source}\n\n'
                        f'{article.hashtags}')
        return message_text

    def send_article(self, article: Article) -> None:
        cache_structure = {
            'bloomberg.com': {
                'last_article_title_hash': ''
            },
            'zerohedge.com': {
                'last_article_title_hash': ''
            }
        }
        if not os.path.exists('auto-sender-cache.json'):
            with open('auto-sender-cache.json', 'w', encoding='utf-8') as file:
                json.dump(cache_structure, file, indent=4)

        with open('auto-sender-cache.json', 'r', encoding='utf-8') as file:
            auto_sender_cache = json.load(file)

        if hashlib.md5(article.title.encode('utf-8')).hexdigest() == auto_sender_cache[article.source]['last_article_title_hash']:
            logger.info('article is duplicate')
            return False

        auto_sender_cache[article.source]['last_article_title_hash'] = hashlib.md5(article.title.encode('utf-8')).hexdigest()

        with open('auto-sender-cache.json', 'w', encoding='utf-8') as file:
            json.dump(auto_sender_cache, file, indent=4)
        
        return True
