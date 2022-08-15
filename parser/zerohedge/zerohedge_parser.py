from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

from parser import ArticleParser
from parser.data_models import Article
from logger import logger


class ZeroHedgeParser(ArticleParser):
    def __init__(self, articles_page_url: str, headless: bool = True) -> None:
        super().__init__(articles_page_url, headless)

    def get_latest_article(self) -> Article:
        logger.info('go to first article')
        self._go_to_first_article_page('h2[class^=Article_title__] > a')
        first_article_soup = bs(self._driver.page_source, 'html.parser')
        article_title = self._driver.find_element(By.CSS_SELECTOR, 'h1[class^=ArticleFull_title__]').text
        print(article_title)
        article_text = self._get_article_text(first_article_soup, 'p')
        print(article_text)
        zerohedge_article = Article(
            title=article_title,
            text=article_text,
            hashtags=self._hashtags,
            source='Zerohedge'
        )
        self._driver.quit()
        return zerohedge_article
