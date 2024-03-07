#!/usr/bin/python3
import uuid
import datetime
class BaseModel:
    """Write a class BaseModel that defines all common attributes/methods for other classes:"""
    def __init__(self):
        """id: string - assign with an uuid when an instance is created:"""
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    def __str__(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        """to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance"""
        new = self.__dict__.copy()
        new['created_at'] = self.created_at.isoformat()
        new['updated_at'] = self.updated_at.isoformat()
        new['__class__'] = self.__class__.__name__
        return new
