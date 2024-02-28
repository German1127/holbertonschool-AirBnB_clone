#!/usr/bin/python3
"""contains the shell entry point"""


import cmd
"""contains the shell entry point"""


class HBNBCommand(cmd.Cmd):
    """class HBNB command """
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Command for quit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Command for quit the program"""
        return True

    def help_EOF(self):
        print("Exit the program on EOF (ctrl-D).")

    def help_quit(self):
        print("Exit the program.")

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
