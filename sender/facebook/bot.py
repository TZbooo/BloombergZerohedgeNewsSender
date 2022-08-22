import time
import textwrap

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from parser.data_models import Article, SocialNetwork
from sender.sender import Sender
from logger import logger


class FacebookSender(Sender):
    def __init__(self, group_url: str, admin_email: str, admin_password: str) -> None:
        self.__group_url = group_url
        self.__admin_email = admin_email
        self.__admin_password = admin_password

    def __create_driver(self) -> None:
        self.__driver = uc.Chrome()
        self.__driver.implicitly_wait(60)
        self.__actions = ActionChains(self.__driver)
        self.__wait = WebDriverWait(self.__driver, 60)

    def send_article(self, article: Article) -> None:
        self.__create_driver()

        self.__login_facebook()

        logger.info('start loading of group page')
        self.__driver.get(self.__group_url)
        time.sleep(15)
        
        # on the group page exists button for create post, code in below move to it and click
        create_post_text_button = self.__wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Write something..."]')))
        logger.info('move viewport to create_post_button')
        self.__actions.move_to_element(create_post_text_button).perform()
        logger.info('click to create post button')
        create_post_text_button.click()
        time.sleep(15)
        
        # generate message text, split it by 10 characters and type parts text to text input for creating post
        message_text = self._get_message_for_send(article, SocialNetwork.FACEBOOK)
        self.__type_text_to_post_text_input(message_text, 'div[aria-label="Create a public post…"]')

        self.__click_create_post_button()
        self.__kill_sender()
        

    def __type_text_to_post_text_input(self, message_text: str, post_text_input_selector: str) -> None: 
        create_post_text_input = self.__driver.find_element(By.CSS_SELECTOR, post_text_input_selector)
        logger.info('generate message_text')
        logger.info('send keys to create_post_text_input')

        # split message by equal 20 characters text parts
        split_message = textwrap.wrap(message_text, 20, replace_whitespace=False, drop_whitespace=False)
        for i in split_message:
            logger.info(f'type {i} to create post input')
            create_post_text_input.send_keys(i)


    def __click_create_post_button(self) -> None: 
        logger.info('create post')
        create_post_button = self.__driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Post"]')
        create_post_button.click()
        time.sleep(15)

    def __login_facebook(self) -> None: 
        logger.info('login facebook')
        self.__driver.get('https://www.facebook.com/')
        email_input = self.__driver.find_element(By.CSS_SELECTOR, '#email')
        password_input = self.__driver.find_element(By.CSS_SELECTOR, '#pass')
        email_input.send_keys(self.__admin_email)
        password_input.send_keys(self.__admin_password)
        self.__driver.find_element(By.XPATH, '//button[text()="Log In"]').click()
        time.sleep(15)

    def __kill_sender(self) -> None: 
        logger.info('close browser')
        self.__driver.close()
        self.__driver.quit()
