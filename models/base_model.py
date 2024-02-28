#!/usr/bin/python3


import uuid
import models
from datetime import datetime


""""class Base"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) is not 0:
            for keys in kwargs:
                if keys != "__class__":
                    if keys == "created_at" or keys == "updated_at":
                        setattr(self, keys, datetime.
                                strptime(kwargs[keys], '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            setattr(self, keys, kwargs[keys])

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict.update({"__class__": self.__class__.__name__})
        instance_dict.update({"created_at": self.created_at.isoformat()})
        instance_dict.update({"updated_at": self.updated_at.isoformat()})

        return instance_dict
