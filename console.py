#!/usr/bin/python3
"""Console module for AirBnB"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_EOF(self, line):
        """Exit the console when EOF is received (Ctrl+D)"""
        return True

    def do_quit(self, line):
        """Quit the console"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print its id"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Print all string representations of instances"""
        args = line.split()
        obj_list = []
        if not args:
            for key in storage.all():
                obj_list.append(str(storage.all()[key]))
            print(obj_list)
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if key.startswith(args[0] + '.'):
                    obj_list.append(str(storage.all()[key]))
            print(obj_list)

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        setattr(obj, attr_name, attr_value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
