#!/usr/bin/python3
"""
Build the BaseModel Class
"""
from datetime import datetime
import models
from uuid import uuid4


class BaseModel():
    """
        BaseModel class define common attributes/methods for other classes

        Args:
            *args: Not used.
            **kwargs: A dict of attributes.
    """

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the pub instance updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """string representation of a BaseModel instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__ of instance"""
        return {
            "__class__": self.__class__.__name__,
            **{
                key: val.isoformat() if isinstance(val, datetime) else
                val for key, val in self.__dict__.items()
               }
        }
