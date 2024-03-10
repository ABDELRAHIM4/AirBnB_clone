import json
import os
from models.base_model import BaseModel
from json import JSONDecodeError
class FileStorage:
    """class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:"""
    __file_path = 'file.json'
    __objects = {}
    def __init__(self):
        """Initializes FileStorage."""
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            self.__objects = {}
    def all(self):
        """all(self): returns the dictionary __objects"""
        return {k: v.to_dict() if isinstance(v, BaseModel) else v for k, v in self.__objects.items()}
    def new(self, obj):
        """new(self, obj): sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}{obj.id}"] =  obj
    def save(self):
        """save(self): serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.all(), file)
    def reload(self):
        """: deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        if os.path.isfile(self.__file_path):
          with open (self.__file_path , 'r') as file:
              data = json.load(file)
