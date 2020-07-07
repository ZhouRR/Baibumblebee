from pydantic import BaseModel


class Media(BaseModel):
    media_id: str = None
    subject: str
    address: str
    key_word: str = None
