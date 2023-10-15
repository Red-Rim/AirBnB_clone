#!/usr/bin/python3


"""Define FileStorage Class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
import os
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    FileStorage class to data

    Attributes:
        __file_path (str): the file to save obj to
        __objects (dict): A dictionary to store instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of all stored objects"""

        return FileStorage.__objects

    def new(self, obj):
        """stores an object on the objects dictionary"""
        objt = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objt, obj.id)] = obj

    def save(self):
        """saves the objects dict on a json file"""
        odct = FileStorage.__objects
        obj_dict = {obj: odct[obj].to_dict() for obj in odct.keys()}
        with open(FileStorage.__file_path, "w") as fil:
            json.dump(obj_dict, fil)

    def reload(self):
        """deserialize json to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as fil:
                obj_dict = json.load(fil)
                for s in obj_dict.values():
                    cls_name = s["__class__"]
                    del s["__class__"]
                    self.new(eval(cls_name)(**s))
        except FileNotFoundError:
            return
