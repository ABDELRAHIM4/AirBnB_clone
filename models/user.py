#!/usr/bin/python3
""" class User that inherits from BaseModel"""
from models.base_model import BaseModel
""" class User that inherits from BaseModel"""
class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def count(self):
        """retrieve the number of instances of a class: <class name>.count()"""
        objs = storage.all()
        count = 0
        for obj in objs.values():
            if type(obj).__name__ == self.__class__.__name__:
                count += 1
        return count
