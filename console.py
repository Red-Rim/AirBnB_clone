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

def is_instance(class_name, base_class_name):
    """Check if class_name is an instance of base_class_name or its subclasses."""
    return class_name in globals() and \
        (class_name == base_class_name or
         issubclass(globals()[class_name], globals()[base_class_name]))

def custom_cmd(expression):
    """Parser function for a custom command expression."""
    pattern = r"(\w+)\.(\w+)(\((.*?)\))?"
    match = re.match(pattern, expression)
    if match:
        groups = match.groups()
        class_name, command, args = (groups[0], groups[1],
                                     groups[3].split(',') if groups[3] else [])
        return ([command, class_name] +
                [element.strip('" ') for element in args if len(args) > 0])
    return []


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
            arguments = argt.split()
            if not is_instance(arguments[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                instance = eval(f"{arguments[0]}()")
                instance.save()
                print(instance.id)

    def do_show(self, argt):
        """Print the string representation of an instance"""
        if not argt:
            print("** class name missing **")
        else:
            arguments = argt.split()
            objects_dict = storage.all()
            if not is_instance(arguments[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            elif f"{arguments[0]}.{arguments[1]}" not in objects_dict.keys():
                print("** no instance found **")
            else:
                key = f"{arguments[0]}.{arguments[1]}"
                obj = objects_dict[key]
                print(obj)

    def do_destroy(self, argt):
        """Deletes an instance based on the class name and id"""
        if not argt:
            print("** class name missing **")
        else:
            arguments = argt.split()
            objects_dict = storage.all()
            if not is_instance(arguments[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            elif f"{arguments[0]}.{arguments[1]}" not in objects_dict.keys():
                print("** no instance found **")
            else:
                class_name, id = arguments
                key = f"{class_name}.{id}"
                del objects_dict[key]
                storage.save()

    def do_all(self, argt):
        """Print all string representations of instances"""
        objects_dict = storage.all()
        if not argt:
            instance_list = [str(objects_dict[obj]) for obj in objects_dict.keys()]
            print(instance_list)
        else:
            arguments = argt.split()
            if not is_instance(arguments[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                instance_list = []
                for key in objects_dict.keys():
                    elements = key.split(".")
                    class_name = elements[0]
                    if class_name == arguments[0]:
                        instance_list.append(str(objects_dict[key]))
                print(instance_list)

    def do_update(self, argt):
        """Update an instance based on the class name and id"""
        objects_dict = storage.all()
        if not argt:
            instance_list = [str(objects_dict[obj]) for obj in objects_dict.keys()]
            print(instance_list)
        else:
            arguments = argt.split()
            if not is_instance(arguments[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                instance_list = []
                for key in objects_dict.keys():
                    elements = key.split(".")
                    class_name = elements[0]
                    if class_name == arguments[0]:
                        instance_list.append(str(objects_dict[key]))
                print(instance_list)

    def do_count(self, argt):
        """
        Count the number of instances of a specific class.
        Usage: <class name>.count()
        """
        count = 0
        if not argt:
            print("** class name missing **")
        else:
            objects_dict = storage.all()
            arguments = argt.split()
            if not is_instance(arguments[0], "BaseModel"):
                print(f"** class doesn't exist **")
            else:
                for key in objects_dict.keys():
                    elements = key.split('.')
                    class_name = elements[0]
                    if class_name == arguments[0]:
                        count += 1
                print(count)

    def do_show(self, argt):
        """
        Show the details of an instance based on its class name and ID.
        Usage: show <class name> <id>
        """
        if not argt:
            print("** class name missing **")
        else:
            arguments = argt.split()
            objects_dict = storage.all()
            if not is_instance(arguments[0], "BaseModel"):
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            elif f"{arguments[0]}.{arguments[1]}" not in objects_dict.keys():
                print("** no instance found **")
            else:
                key = f"{arguments[0]}.{arguments[1]}"
                obj = objects_dict[key]
                print(obj)


if __name__ == '__main__':

    HBNBCommand().cmdloop()
