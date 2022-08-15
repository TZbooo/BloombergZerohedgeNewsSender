import time

import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs


class ArticleParser:
    def __init__(self, articles_page_url: str, headless: bool) -> None:
        self._articles_page_url = articles_page_url
        self._hashtags = [
            '#financialplanningservices', 
            '#invesmentportfolio',
            '#CFA', 
            '#financialplanningprofession']
        options = ChromeOptions()
        options.headless = headless
        driver = uc.Chrome(options=options)
        driver.implicitly_wait(20)
        self._driver = driver

    def _go_to_first_article_page(self, first_article_link_selector: str) -> str:
        self._driver.get(self._articles_page_url)

        # когда ты, тестируя, будешь запускать этот парсер слишком часто,
        # ты увидишь сообщение о подозрительной активности, если ты увидел это сообщение -- 
        # раскомментируй этот код и нажми, удерживая, 
        # на кнопку press & hold, останови программу и снова закомментируй

        # time.sleep(300)
        first_article_url = self._driver.find_element(By.CSS_SELECTOR, first_article_link_selector).get_attribute('href')
        self._driver.get(first_article_url)

    def _get_article_text(self, article_soup: bs, text_selector: str):
        article_text = [i.text for i in article_soup.select(text_selector) if i.text]
        return article_text
