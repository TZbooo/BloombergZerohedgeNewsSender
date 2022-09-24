from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup as bs
import undetected_chromedriver as uc


class ArticlesParser:
    def __init__(self, articles_page_url: str, source: str) -> None:
        self._articles_page_url = articles_page_url
        self._source = source
        self._hashtags = ('#financialplanningservices '
                         '#invesmentportfolio '
                         '#CFA '
                         '#financialplanningprofession')
                         
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--user-data-dir=selenium')
        chrome_options.add_argument('--no-sandbox')
        driver = uc.Chrome(options=chrome_options)
        driver.implicitly_wait(20)
        self._driver = driver

    def _go_to_first_article_page(self, first_article_link_selector: str) -> str:
        self._driver.get(self._articles_page_url)
        articles_page_soup = bs(self._driver.page_source, 'html.parser')

        first_article_url = articles_page_soup.select_one(first_article_link_selector).get('href')
        if self._source == 'zerohedge.com':
            first_article_url = self._articles_page_url + first_article_url
        
        self._driver.get(first_article_url)
        first_article_soup = bs(self._driver.page_source, 'html.parser')
        return first_article_soup

    def _get_article_text(self, article_soup: bs, text_selector: str):
        article_text = [i.text for i in article_soup.select(text_selector) if i.text]
        return article_text
