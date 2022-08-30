from dataclasses import dataclass


class Article:
    def __init__(self, title, text, hashtags, source):
        self.title = title
        self.text = text
        self.hashtags = hashtags
        self.source = source


class SocialNetwork:
    TELEGRAM = 'TELEGRAM'
    FACEBOOK = 'FACEBOOK'
