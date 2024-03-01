import json
from amenity import Amenity
from base_model import BaseModel
from city import City
from place import Place
from review import Review
from state import State
from user import User


class FileStorage:
    """class that serializes instances to a JSON file and
    deserializes the JSON file into instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public instance method that return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """public instance method that sets in __objects
        the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """public instance method that serializes __objects to the JSON file"""
        serialized_obj = {}
        for key, obj in self.__objectis.items():
            serialized_obj[key] = obj.to_dic()
        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_obj, json_file)

    def reload(self):
        """public instance method that deserializes the JSON
        file to __objects"""
        clases = {
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
                    clasname = x["__class__"]
                    self.new(clases[clasname](**x))

        except FileNotFoundError:
            pass
