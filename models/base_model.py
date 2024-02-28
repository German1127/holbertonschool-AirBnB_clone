#!/usr/bin/python3


import uuid
import models
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.
                                strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, kwargs[key])

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     getattr(self, 'id', None), self.__dict__)

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        if 'created_at' in instance_dict:
            instance_dict['created_at'] =
            instance_dict['created_at'].isoformat()
        if 'updated_at' in instance_dict:
            instance_dict['updated_at'] =
            instance_dict['updated_at'].isoformat()
        return instance_dict
