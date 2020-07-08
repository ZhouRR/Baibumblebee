from models.models import *
from utils import request_utils

from bs4 import BeautifulSoup
from newspaper import Article


def parse_target_url(soup):
    a_tags = soup.find_all('a')
    target_url = str(a_tags[len(a_tags) - 1]['href'])
    return target_url


def get_contents():
    return []


def post_contents(headline: HeadLine):
    resp_body = request_utils.get(headline.href.replace('./', headline.href_head))
    soup = BeautifulSoup(resp_body, 'lxml')
    result = [soup.title.string, ]

    contents = []
    if headline.media_id == '002':
        target_url = parse_target_url(soup)
        article = Article(target_url, language='zh')
        article.download()
        article.parse()
        contents += [article.text, ]

    result += [contents, ]
    return result
