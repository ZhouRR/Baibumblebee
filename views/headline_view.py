from models.models import *
from utils import request_utils


def get_headlines():
    medias = []
    medias += [{'media_id': '001',
                'subject': 'yahoo',
                'address': 'https://news.yahoo.co.jp/',
                'key_word': ''}, ]
    medias += [{'media_id': '002',
                'subject': 'google',
                'address': 'https://news.google.com/search?q={0}&hl=zh-CN&gl=CN&ceid=CN%3Azh-Hans',
                'key_word': ''}, ]
    return medias


def post_headlines(media: Media):
    resp_body = request_utils.get(media.address.replace('{0}', media.key_word))
    return resp_body
