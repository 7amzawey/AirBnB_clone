#!/usr/bin/python3
import cmd
"""this module is for difining a class console.py"""


class HBNBCommand(cmd.Cmd):
    """the interactive mode with HBNB website"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help information for Quit"""
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
