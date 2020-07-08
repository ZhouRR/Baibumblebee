from models.models import *
from utils import request_utils

import numpy as np

from bs4 import BeautifulSoup


def get_headlines():
    return []


def post_headlines(media: Media):
    resp_body = request_utils.get(media.address.replace('{0}', media.key_word))
    soup = BeautifulSoup(resp_body, 'lxml')
    result = [soup.title.string, ]
    main_tag = soup.main
    headlines = np.array(main_tag.strings)
    headlines = np.array_split(headlines, len(main_tag.strings)/9+1)
    result += [headlines, ]
    return result
