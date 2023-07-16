#!/usr/bin/python3
"""This is the HBNB console"""



import json
import models
import cmd
from models.user import User
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models import storage
from models.amenity import Amenity
from models.state import State




class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb) "
    classes_hbnb = ["BaseModel", "Place", "User",  "State\
", "City", "Review" , "Amenity"]

    def do_quit(self, args):
        """Quits the console"""
        return True

    def do_EOF(self, args):
        """EOF to quit"""
        return True

    def emptyline(self):
        """Perform nothing when there's no commmand passed to the console"""
        pass

    def create(self, args):
        """Creates new instance and saves it to a json file"""
        if args == "":
            print("** class name missing **")
        elif args not in HBNBCommand.classes_hbnb:
            print("** class doesn't exist **")
        else:
            a = eval(args)()
            print(a.id)
            a.save()

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id"""
        sw = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes_hbnb:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            if_keyis = (arg[0] + "." + arg[1])
            for key, obj in storage.all().items():
                if key == if_keyis:
                    print(obj)
                    wb = 1
            if wb == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        updating JSON file\nUsage: (hbnb) destroy <class_name> <class_id>"""
        sw = 0
        arg = args.split()
        if args == "":
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes_hbnb:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            if_keyis = (arg[0] + "." + arg[1])
            dictionary_obs = storage.all()
            for key, obj in dictionary_obs.items():
                if key == if_keyis:
                    del dictionary_obs[key]
                    wb = 1
                    storage.save()
                    storage.reload()
                    return
            if wb == 0:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        list_ = []
        if args == "":
            for key, obj in storage.all().items():
                all_list.append(str(obj))
            print(all_list)
        elif args in HBNBCommand.classes_hbnb:
            for key, obj in storage.all().items():
                if args == key.split(".")[0]:
                    all_list.append(str(obj))
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute, saving on JSON file"""
        arg = args.split()
        wb = 0
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes_hbnb:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            if_keyis = (arg[0] + "." + arg[1])
            for key, obj in storage.all().items():
                if key == if_keyis:
                    args_idss = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    value = args[args_idss:]
                    if args[args_idss] == "\"":
                        args_idss += 1
                        value = args[args_idss:-1]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, arg[2]))(args[args_idss:])
                    setattr(obj, arg[2], value)
                    wb = 1
                    storage.save()
            if wb == 0:
                print("** no instance found **")
                return -1

    def default(self, args):
        """This makes action when command is typed"""
        count = 0
        if len(args.split(".")) > 1:
            ClassName = args.split(".")[0]
            if ClassName in HBNBCommand.classes_hbnb:
                try:
                    if args.split(".")[1] == "all()":
                        self.all(ClassName)
                    if args.split(".")[1] == "count()":
                        for key, obj in storage.all().items():
                            if key.split(".")[0] == ClassName:
                                count += 1
                        print(count)
                    if args.split(".")[1].split("(")[0] == "show":
                        is_id = args.split("\"")[1].split("\"")[0]
                        self.show(ClassName + " " + is_id)
                    if args.split(".")[1].split("(")[0] == "destroy":
                        is_id = args.split("\"")[1].split("\"")[0]
                        self.destroy(ClassName + " " + is_id)
                    if args.split(".")[1].split("(")[0] == "update":
                        list_args = args.split(".", 1)[1]
                        list_args = list_args.split("(")[1][:-1].split(",")
                        if "{" not in list_args[1]:
                            is_id = list_args[0][1:-1]
                            name = list_args[1][2:-1]
                            value = list_args[2][1:]
                            if value[0] == "\"":
                                value = value[1:-1]
                            self.update(ClassName + "\
 " + is_id + " " + name + " " + value)
                        else:
                            is_id = list_args[0][1:-1]
                            dicts_args = args.split(".")[1]
                            dicts_args = dicts_args.split("(")[1][:-1]
                            dicts_args = dicts_args.split("{")[1]
                            dicts_args = "{" + dicts_args
                            dictionary = eval(dicts_args)
                            for key, value in dictionary.items():
                                ret = self.update(ClassName + "\
 " + is_id + " " + key + " " + str(value))
                                if ret == -1:
                                    break
                except Exception:
                    cmd.Cmd.default(self, args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == "__main__":
    comand = HBNBCommand()
    comand.cmdloop()

