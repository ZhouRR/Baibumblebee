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
    main_tag_strings = []
    main_tag = soup.main
    for child in main_tag.strings:
        main_tag_strings += [str(child), ]

    headlines = []
    for i in get_index(main_tag_strings, 'more_vert'):
        if i + 9 >= len(main_tag_strings):
            break
        headline = {
            'title': main_tag_strings[i + 1],
            'preview': main_tag_strings[i + 2],
            'source': main_tag_strings[i + 5],
            'datetime': main_tag_strings[i + 6]
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
