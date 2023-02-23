#!/usr/bin/python3
"""Write a class BaseModel that defines all common
attributes/methods for other classes:
"""
import uuid
import datetime
import models


class BaseModel:
    """
    * Public instance attributes:
        * you will use *args, **kwargs arguments for the
        constructor of a BaseModel.
        (more information inside the AirBnB clone concept page)args
        won’t be used
        * if kwargs is not empty:
        * each key of this dictionary is an attribute name
        (Note __class__ from kwargs
        is the only one that should not be added as an attribute.
        See the example output, below)
        * each value of this dictionary is the value of this attribute name
        * Warning: created_at and updated_at are strings in this dictionary,
        but inside your BaseModel instance is working with datetime object.
        You have to convert these strings into datetime object. Tip: you know
        the string format of these datetime
        otherwise:
        * create id and created_at as you did previously (new instance)
    """

    def __init__(self, name="", my_number=0, *args, **kwargs):
        self.my_number = my_number
        self.name = name
        if (kwargs):
            for i in kwargs:
                if i == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        (kwargs[i]), '%Y-%m-%dT%H:%M:%S.%f')
                if i == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                        (kwargs[i]), '%Y-%m-%dT%H:%M:%S.%f')
                if i == "id":
                    self.id = kwargs[i]

        else:
            self.updated_at = (datetime.datetime.now())
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.datetime.now())
            models.storage.new(self)

    def __str__(self):
        """
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>"
        """
        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """
        save(self): updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = (datetime.datetime.now())
        models.storage.save()

    def to_dict(self):
        """
        : returns a dictionary containing all keys/values of
         __dict__ of the instance:
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of
        the object
        created_at and updated_at must be converted to string object
        in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)you
        can use
        isoformat() of datetime object
        """
        dict = self.__dict__.copy()
        dict["updated_at"] = (self.updated_at.isoformat())
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = (self.created_at.isoformat())
        return (dict)
