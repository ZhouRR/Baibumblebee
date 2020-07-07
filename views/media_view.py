from models.models import *


def get_medias():
    medias = []
    medias += [{'media_id': '001',
                'subject': 'yahoo',
                'address': 'https://news.yahoo.co.jp/',
                'key_word': ''}, ]
    medias += [{'media_id': '002',
                'subject': 'google',
                'address': 'https://news.google.com/',
                'key_word': ''}, ]
    return medias


def post_medias(media: Media):
    return "push media finished"
