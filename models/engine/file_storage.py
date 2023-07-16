#!/usr/bin/python3
"""FileStorage class container"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os.path
import json


class FileStorage():
    """file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this returns the object"""
        return FileStorage.__objects

    def new(self, obj):
        """
        new method
        """
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        save to a json file
        """
        d = {}
        for key, obj in FileStorage.__objects.items():
            d[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(d, json_f)

    def reload(self):
        """
        reloads object
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = obj

