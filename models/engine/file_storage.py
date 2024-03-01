#!/usr/bin/python3
"""JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class that handles serialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """method that sets in objects the object <obj>"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """method that serializes objects to a JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file_guard:
            json.dump(serialized_objs, file_guard, indent=4)

    def reload(self):
        """method that deserializes"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as guard:
                serialized_objs = json.load(guard)
                for x in serialized_objs.values():
                    classname = x["__class__"]
                    self.new(classes[classname](**x))

        except FileNotFoundError:
            pass
