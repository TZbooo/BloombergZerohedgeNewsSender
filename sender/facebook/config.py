import os

from dotenv import load_dotenv


load_dotenv()

FACEBOOK_GROUP_URL = 'https://www.facebook.com/groups/766101074714931'
FACEBOOK_ADMIN_EMAIL = os.getenv('FACEBOOK_ADMIN_EMAIL')
FACEBOOK_ADMIN_PASSWORD = os.getenv('FACEBOOK_ADMIN_PASSWORD')
