#!/usr/bin/python3
"""
Defines BaseModel class
"""

from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """
    Base class defines common attribute & methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the `BaseModel` class.

        Args:
            *args: Any additional positional arguments, if required.
            **kwargs: Any additional keyword arguments, if required.

        Attributes:
            id (str): A unique identifier for this object.
            created_at (datetime): The timestamp indicating when this object was created.
            updated_at (datetime): The timestamp indicating when this object was last updated.
        """
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a descriptor of the object.
        Return:
        str: A brief description or identifier for the object.
        """
        return ("[{}] ({}) {}\
".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save method that save time update and update
        the updated_at instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method that get an prepared dict
        Return:
            new dictionary
        """
        dictionary = {}
        for key in self.__dict__:
            dictionary[key] = self.__dict__[key]
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
