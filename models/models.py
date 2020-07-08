from pydantic import BaseModel


class Media(BaseModel):
    media_id: str = None
    subject: str
    address: str
    key_word: str = None


class HeadLine(BaseModel):
    media_id: str
    href: str
    href_head: str
    title: str = None
    preview: str = None
    source: str = None
    datetime: str = None
