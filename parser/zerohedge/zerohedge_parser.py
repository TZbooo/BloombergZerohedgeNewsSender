import time

from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

from parser import Parser
from parser.config import ZEROHEDGE_ARTICLES_PAGE_URL
from parser.data_models import Article


class ZeroHedgeParser(Parser):
    def __init__(self, articles_page_url: str) -> None:
        super().__init__(articles_page_url)

    def get_latest_article(self) -> Article:
        self._driver.get(self._articles_page_url)
        first_article_url = self._driver.find_element(By.CSS_SELECTOR, 'h2[class^=Article_title__] > a').get_attribute('href')
        self._driver.get(first_article_url)
        first_article_soup = bs(self._driver.page_source, 'html.parser')
        article_title = self._driver.find_element(By.CSS_SELECTOR, 'h1[class^=ArticleFull_title__]').text
        article_text = [i.text for i in first_article_soup.select('p') if i.text]
        zerohedge_article = Article(
            title=article_title,
            text=article_text,
            hashtags=self._hashtags,
            source='Zerohedge'
        )
        return zerohedge_article


if __name__ == '__main__':
    zerohedge = ZeroHedgeParser(ZEROHEDGE_ARTICLES_PAGE_URL)
    m = zerohedge.get_latest_article()
    print(m.text)
    print(m.title)