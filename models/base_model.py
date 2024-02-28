#!/usr/bin/python3
"""class BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """init atributes of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "update_at"):
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)