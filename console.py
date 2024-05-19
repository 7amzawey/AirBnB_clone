#!/usr/bin/python3
"""this module is for difining a class console.py"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """the interactive mode with HBNB website"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates a new Instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif (args != "BaseModel"):
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            print(new_model.id)

    def do_show(self, args):
        """prints the string representation of an instance based on the class
        name adn id"""
        if not args:
            print("** class name missing **")
            return

        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        insta_id = arg[1]
        key = "{}.{}".format(class_name, insta_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, args):
        """deletes an instance based on the class name and id save the change
        into the json file"""
        if not args:
            print("** class name missing **")
            return

        arg = args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return

        class_name = arg[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        insta_id = arg[1]
        key = "{}.{}".format(class_name, insta_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """prints all string representation of all instances based or not on
        class name."""
        if arg != "BaseModel":
            print("** class doesn't exist **")

        elif not arg or arg == "BaseModel":
            storage.__str__()

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
