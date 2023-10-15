#!/usr/bin/python3
"""define console module for AirBnB clone"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not args:
            print("Error: Missing class name for the create command.")
        else:
            try:
                new_instance = eval(args)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("Error: Class doesn't exist for create command.")

    def do_show(self, args):
        """Print the string representation of an instance"""
        args = args.split()
        if not args:
            print("Error: Missing class name for the show command.")
        elif args[0] not in storage.classes:
            print("Error: Class doesn't exist for show command.")
        elif len(args) < 2:
            print("Error: Missing instance id for the show command.")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("Error: No instance found with the specified id.")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("Error: Missing class name for the destroy command.")
        elif args[0] not in storage.classes:
            print("Error: Class doesn't exist for destroy command.")
        elif len(args) < 2:
            print("Error: Missing instance id for the destroy command.")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("Error: No instance found with the specified id.")

    def do_all(self, args):
        """Print all string representations of instances"""
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args not in storage.classes:
            print("Error: Class doesn't exist for all command.")
        else:
            l = args
            print([str(obj) for key, obj in objects.items() if key.split('.')[0] == l])

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("Error: Missing class name for the update command.")
        elif args[0] not in storage.classes:
            print("Error: Class doesn't exist for update command.")
        elif len(args) < 2:
            print("Error: Missing instance id for the update command.")
        elif len(args) < 3:
            print("Error: Missing attribute name for the update command.")
        elif len(args) < 4:
            print("Error: Missing attribute value for the update command.")
        else:
            obj_key = args[0] + '.' + args[1]
            objects = storage.all()
            if obj_key in objects:
                obj = objects[obj_key]
                atr_name = args[2]
                atr_value = args[3]
                if atr_name in obj.__class__.__dict__:
                    # Check the attribute type and cast the value
                    if isinstance(atr_value, int):
                        atr_value = int(atr_value)
                    elif isinstance(atr_value, float):
                        atr_value = float(atr_value)
                    elif isinstance(atr_value, str):
                        atr_value = str(atr_value)
                    else:
                        print("Error: Invalid attribute type for the update command.")
                        return
                    setattr(obj, atr_name, atr_value)
                    obj.save()
                else:
                    print("Error: Attribute doesn't exist for the update command.")
            else:
                print("Error: No instance found with the specified id.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
