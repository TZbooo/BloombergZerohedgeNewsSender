import time

import requests
import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs


class ArticlesParser:
    def __init__(self, articles_page_url: str, source: str, headless: bool) -> None:
        self._articles_page_url = articles_page_url
        self._source = source
        self._hashtags = [
            '#financialplanningservices', 
            '#invesmentportfolio',
            '#CFA', 
            '#financialplanningprofession']
        options = ChromeOptions()
        options.headless = headless
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"
        driver = uc.Chrome(options=options, desired_capabilities=caps)
        driver.implicitly_wait(20)
        self._driver = driver

    def _go_to_first_article_page(self, first_article_link_selector: str) -> str:
        self._driver.get(self._articles_page_url)
        time.sleep(20)
        articles_page_soup = bs(self._driver.page_source, 'html.parser')

        # когда ты, тестируя, будешь запускать этот парсер слишком часто,
        # ты увидишь сообщение о подозрительной активности, если ты увидел это сообщение -- 
        # раскомментируй этот код и нажми, удерживая, 
        # на кнопку press & hold, останови программу и снова закомментируй
        # time.sleep(300)
        first_article_url = articles_page_soup.select_one(first_article_link_selector).get('href')
        if self._source == 'ZEROHEDGE':
            first_article_url = self._articles_page_url + first_article_url
        print(first_article_url)
        self._driver.get(first_article_url)
        time.sleep(20)
        first_article_soup = bs(self._driver.page_source, 'html.parser')
        return first_article_soup

    def _get_article_text(self, article_soup: bs, text_selector: str):
        article_text = [i.text for i in article_soup.select(text_selector) if i.text]
        return article_text
