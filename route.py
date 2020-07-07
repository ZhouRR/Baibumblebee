import os

from fastapi import FastAPI

import urls
from models.models import *
from views import media_view, headline_view

app = FastAPI()


@app.get(urls.MEDIAS)
async def get_medias():
    return media_view.get_medias()


@app.post(urls.MEDIAS)
async def post_medias(media: Media):
    return media_view.post_medias(media)


@app.get(urls.HEAD_LINES)
async def get_headlines():
    return headline_view.get_headlines()


@app.post(urls.HEAD_LINES)
async def post_headlines(media: Media):
    return headline_view.post_headlines(media)


def execute_from_command_line(cmd=None):
    os.system(cmd)


def main():
    execute_from_command_line('uvicorn route:app --reload')
    pass


if __name__ == '__main__':
    main()
