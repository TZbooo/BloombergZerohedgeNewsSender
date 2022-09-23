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
