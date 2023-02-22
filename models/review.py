#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
    def __str__(self):
        return (f"[Review] ({self.id}) {self.__dict__}")