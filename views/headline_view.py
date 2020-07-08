from models.models import *
from utils import request_utils

from bs4 import BeautifulSoup


def get_headlines():
    return []


def post_headlines(media: Media):
    resp_body = request_utils.get(media.address.replace('{0}', media.key_word))
    soup = BeautifulSoup(resp_body, 'lxml')
    result = [soup.title.string, ]
    main_tag = soup.main
    for child in main_tag.strings:
        result += [child, ]
    return result
