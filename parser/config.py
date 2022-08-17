import os

from dotenv import load_dotenv


load_dotenv()

BLOOMBERG_ARTICLES_PAGE_URL = os.getenv('BLOOMBERG_ARTICLES_PAGE_URL')
ZEROHEDGE_ARTICLES_PAGE_URL = os.getenv('ZEROHEDGE_ARTICLES_PAGE_URL')