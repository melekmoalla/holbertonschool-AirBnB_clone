#!/usr/bin/python3


from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __str__(self):
        return (f"[State] ({self.id}) {self.__dict__}")
