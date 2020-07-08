import os

from fastapi import FastAPI

import urls
from models.models import *
from views import media_view, headline_view, contents_view

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


@app.get(urls.CONTENTS)
async def get_contents():
    return contents_view.get_contents()


@app.post(urls.CONTENTS)
async def post_contents(headline: HeadLine):
    return contents_view.post_contents(headline)


def execute_from_command_line(cmd=None):
    os.system(cmd)


def main():
    execute_from_command_line('uvicorn route:app --reload --host 0.0.0.0 --port 8000')
    pass


if __name__ == '__main__':
    main()
