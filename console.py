#!/usr/bin/python3
"""define console module for AirBnB clone"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, argt):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, argt):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, argt):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not argt:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(argt)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, argt):
        """Print the string representation of an instance"""
        args = argt.split()
        if not argt:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, argt):
        """Deletes an instance based on the class name and id"""
        args = argt.split()
        if not argt:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argt):
        """Print all string representations of instances"""
        objects = storage.all()
        if not argt:
            print([str(obj) for obj in objects.values()])
        elif argt not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.split('.')[0] == l])

    def do_update(self, argt):
        """Update an instance based on the class name and id"""
        args = argt.split()
        if not argt:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                obj = objects[obj_key]
                atr_name = args[2]
                atr_value = args[3]
                if atr_name in obj.__class__.__dict__:
                    atr_value = type(obj.__class__.__dict__[atr_name])
                    (atr_value)
                    setattr(obj, atr_name, atr_value)
                    obj.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_count(self, argt):
        """
        Count the number of instances of a specific class.
        Usage: <class name>.count()
        """
        args = argt.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
            print(count)

    def do_show(self, argt):
        """
        Show the details of an instance based on its class name and ID.
        Usage: show <class name> <id>
        """
        args = argt.split()
        if not argt:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
