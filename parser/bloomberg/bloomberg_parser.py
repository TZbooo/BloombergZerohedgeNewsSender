import time

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

from parser.data_models import Article
from parser import ArticleParser


class BloombergParser(ArticleParser):
    def __init__(self, articles_page_url, headless: bool = True):
        super().__init__(articles_page_url, headless)

    def get_latest_article(self) -> Article:
        self._go_to_first_article_page('div[class^=storyItem__] > a')
        first_article_soup = bs(self._driver.page_source, 'html.parser')
        article_title = self._driver.find_element(By.CSS_SELECTOR, 'h1[class^=headline__]').text
        article_text = self._get_article_text(first_article_soup, 'div[class^=body-content] > p, div[class^=body-content] > h2[class=paywall], div[class^=body-content] > ul[class=paywall]')
        bloomberg_article = Article(
            title=article_title,
            text=article_text,
            hashtags=self._hashtags,
            source='Bloomberg')
        self._driver.quit()
        return bloomberg_article