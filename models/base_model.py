#!/usr/bin/python3
"""class BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """init atributes of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """return string of the class name, id and dict"""
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute"""
        self.update_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of"""
        dic = self.__dict__.copy()
        dic['__class__'] = __class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
