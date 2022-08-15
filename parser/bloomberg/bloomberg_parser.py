import time

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

from parser.data_models import Article
from parser import ArticleParser
from logger import logger


class BloombergParser(ArticleParser):
    def __init__(self, articles_page_url: str, headless: bool = True) -> None:
        super().__init__(articles_page_url, 'BLOOMBERG', headless)

    def get_latest_article(self) -> Article:
        first_article_soup = self._go_to_first_article_page('div[class^=storyItem__] > a')
        logger.info('go to first article')
        article_title = first_article_soup.select_one('h1[class^=headline__]').text
        logger.info(f'article {article_title} start parsing')
        article_text = self._get_article_text(first_article_soup, 'div[class^=body-content] > p, div[class^=body-content] > h2[class=paywall], div[class^=body-content] > ul[class=paywall]')
        bloomberg_article = Article(
            title=article_title,
            text=article_text,
            hashtags=self._hashtags,
            source='Bloomberg')
        self._driver.quit()
        return bloomberg_article
