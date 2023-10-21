#!/usr/bin/python3
"""Defines BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base class defines """

    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel.

            Args:
                *args : no args.
                **kwargs : key/value pairs.
        """
        arc = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for c, u in kwargs.items():
                if c == "created_at" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(u, tf)
                else:
                    self.__dict__[c] = u
        else:
            models.storage.new(self)

    def save(self):
        """
	Update the 'updated_at' public instance attribute with the current date and time, and save the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """
        Returns a string in format :[<class name>] (<self.id>) <self.__dict__>
        """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
