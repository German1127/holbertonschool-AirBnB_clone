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
    
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }
    def default(self, arg):
        """Default Metod that matches arguments."""

        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "create": self.do_create,
            "update": self.do_update,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
