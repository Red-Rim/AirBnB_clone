#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the ID."""
        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and ID."""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        obj = storage.get(args[0], args[1])
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and ID."""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        obj = storage.get(args[0], args[1])
        if not obj:
            print("** no instance found **")
        else:
            storage.delete(obj)
            storage.save()

    def do_all(self, line):
        """Prints string representation of all instances based on the class name."""
        args = line.split()
        if not line or args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        objs = storage.all(args[0])
        print([str(obj) for obj in objs.values()])

    def do_update(self, line):
        """Updates an instance based on the class name and ID."""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + "." + args[1]
        obj = storage.get(args[0], args[1])
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(obj, attr_name):
            try:
                attr_value = eval(attr_value)
            except Exception:
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
