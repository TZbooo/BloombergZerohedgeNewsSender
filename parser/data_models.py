from dataclasses import dataclass


@dataclass
class Article:
    title: str
    text: str
    hashtags: list[str]
    source: str


class SocialNetwork:
    TELEGRAM = 'TELEGRAM'
