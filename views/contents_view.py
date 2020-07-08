from models.models import *
from utils import request_utils

from bs4 import BeautifulSoup


def get_contents():
    return []


def post_contents(headline: HeadLine):
    resp_body = request_utils.get(headline.href.replace('./', headline.href_head))
    soup = BeautifulSoup(resp_body, 'lxml')
    result = [soup.title.string, ]

    contents = []
    result += [contents, ]
    return resp_body
