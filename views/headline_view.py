from models.models import *
from utils import request_utils

from collections import defaultdict
from bs4 import BeautifulSoup


def get_index(source_list, key):
    index_dict = defaultdict(list)
    index_dict[key].append(-1)
    for k, va in [(v, i) for i, v in enumerate(source_list)]:
        index_dict[k].append(va)
    return index_dict[key]


def parse_google(soup):
    tag_strings = []
    article_tags = soup.find_all('article')
    for article_tag in article_tags:
        tag_strings += [str(article_tag.a['href']), ]
        for child in article_tag.strings:
            tag_strings += [str(child), ]

    headlines = []
    for i in get_index(tag_strings, 'more_vert'):
        if i + 9 >= len(tag_strings):
            break
        headline = {
            'href': tag_strings[i + 1],
            'title': tag_strings[i + 2],
            'preview': tag_strings[i + 3],
            'source': tag_strings[i + 6],
            'datetime': tag_strings[i + 7]
        }
        headlines += [headline, ]
    return headlines


def get_headlines():
    return []


def post_headlines(media: Media):
    resp_body = request_utils.get(media.address.replace('{0}', media.key_word))
    soup = BeautifulSoup(resp_body, 'lxml')
    result = [soup.title.string, ]

    headlines = []
    if media.media_id == '002':
        headlines = parse_google(soup)
    result += [headlines, ]
    return result
