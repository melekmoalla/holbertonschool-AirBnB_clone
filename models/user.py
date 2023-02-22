#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        return (f"[user] ({self.id}) {self.__dict__}")