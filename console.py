#!/usr/bin/python3
"""this module is for difining a class console.py"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the interactive mode with HBNB website"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates a new Instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return

        if (args != "BaseModel") and (args != "User"):
            print("** class doesn't exist **")
            return

        if args == "BaseModel":
            new_model = BaseModel()
        elif args == "User":
            new_model = User()

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
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return

        objects = storage.all()
        instances = []

        if not arg:
            """print all instances"""
            for obj in objects.values():
                instances.append(str(obj))
        else:
            for key, obj in objects.items():
                if key.startswith("BaseModel."):
                    instances.append(str(obj))
        print(instances)

    def do_update(self, args):
        """updates an isntance based on the class name and id by adding or
        updating attribute (save the changes into the json file"""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        if len(arg_list) < 1:
            print("** class name missing **")
            return

        cls_name = arg_list[0]
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        cls_id = arg_list[1]
        key = "{}.{}".format(cls_name, cls_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        attr_name = arg_list[2]

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attr_value = arg_list[3]
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        instance = instances[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

        storage.save()

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
