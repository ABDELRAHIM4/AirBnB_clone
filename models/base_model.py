#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods for other classes:"""
import uuid
import datetime
from models.__init__ import storage
from models.engine.file_storage import FileStorage
class BaseModel:
    """Write a class BaseModel that defines all common attributes/methods for other classes:"""
    def __init__(self, *args, **kwargs):
        """id: string - assign with an uuid when an instance is created:"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if self.id is None:
            storage.new(self)
        if kwargs != None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self,key,value)
                self.created_at == self.updated_at == datetime.datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at == self.updated_at == datetime.datetime.utcnow()

    def __str__(self):
        """__str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """save(self): updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        """call save(self) method of storage"""
        storage = FileStorage()
        storage.save()
    def to_dict(self):
        """to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key[0] != "_":
                dictionary[key] = value
            else:
                continue
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
    def count(self):
        """retrieve the number of instances of a class: <class name>.count().:"""
        objs = storage.all()
        count = 0
        for obj in objs.values():
            if type(obj).__name__ == self.__class__.__name__:
                count += 1
        return count
    @staticmethod
    def all():
        """Returns a dictionary of all instances of the class"""
        return storage.all()
    @staticmethod
    def count(class_name):
        """Returns the number of instances of the class"""
        objs = storage.all()
        count = 0
        if objs:
            for value in objs.values():
                if type(value).__name__ == class_name:
                    count += 1
        return count
