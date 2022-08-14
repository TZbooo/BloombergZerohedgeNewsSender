from selenium.webdriver.common.by import By

from parser.config import BLOOMBERG_ARTICLES_PAGE_URL
from parser.data_models import Article
from parser import Parser


class BloombergParser(Parser):
    def __init__(self, articles_page_url):
        super().__init__(articles_page_url)

    def get_latest_article(self) -> Article:
        self._driver.get(self._articles_page_url)
        self._driver.get(self._driver.find_element(By.CSS_SELECTOR, 'div[class^=storyItem__] > a').get_attribute('href'))
        article_title = self._driver.find_element(By.CSS_SELECTOR, 'h1[class^=headline__]').text
        article_text = [i.text for i in self._driver \
            .find_elements(
                By.CSS_SELECTOR, 
                'div[class^=body-content] > p, div[class^=body-content] > h2[class=paywall], div[class^=body-content] > ul[class=paywall]')
                if i.text]
        bloomberg_article = Article(
            title=article_title, 
            text=article_text,
            hashtags=self._hashtags,
            source='Bloomberg')
        return bloomberg_article


if __name__ == '__main__':
    bloomberg = BloombergParser(BLOOMBERG_ARTICLES_PAGE_URL)
    m = bloomberg.get_latest_article()
    print(m.title, m.text, m.hashtags, m.source, sep='\n\n')