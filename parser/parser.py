import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions


class Parser:
    def __init__(self, articles_page_url: str) -> None:
        self._articles_page_url = articles_page_url
        self._hashtags = [
            '#financialplanningservices', 
            '#invesmentportfolio',
            '#CFA', 
            '#financialplanningprofession']
        options = ChromeOptions()
        driver = uc.Chrome(options=options)
        driver.implicitly_wait(20)
        self._driver = driver