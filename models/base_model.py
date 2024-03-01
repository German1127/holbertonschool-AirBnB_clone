#!/usr/bin/python3
"""Class base"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "__class__":
                        continue
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, timeformat)
                    else:
                        self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        direc = self.__dict__.copy()
        direc["__class__"] = type(self).__name__
        direc["created_at"] = self.created_at.isoformat()
        direc["updated_at"] = self.updated_at.isoformat()
        return direc
