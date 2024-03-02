#!/usr/bin/python3
"""contains the shell entry point"""


import cmd
import re
import json

from shlex import split
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNB command """
    prompt = "(hbnb)"
    
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Method that quits the program."""
        return True

    def do_EOF(self, arg):
        """Method for the end of file."""
        return True

    def help_quit(self):
        """Method that manages the help for the commands.s"""

        print("Quit command to exit the program.")

    def help_create(self):
        """Method that manages the help commando for the create method."""
        print("Create command to create a new insance.")

    def help_show(self):
        """Method that manages the help command for the show method."""
        print("Show command prints on screen infromation about instances.")

    def help_destroy(self):
        """Method that manages the help command for the destroy method."""
        print("Destroy command deletes instances.")

    def help_all(self):
        """Method that manages the help command for the all method."""
        print("All command displays all of the instances.")

    def help_EOF(self):
        """Method that manages the help command for the EOF method."""
        print("EOF command exits the program.")

    def help_update(self):
        """ Method that manages the help command for the update method. """
        print("The Update command updates the class information.")
        
    def emptyline(self):
        """Method that creates an emppty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
