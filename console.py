#!/usr/bin/python3

"""Importing dependancies"""
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """class that runs the console"""
    __classes = {
                "BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                }
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quits the console
        """
        return True

    def do_EOF(self, args):
        """
        Quits the console
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of class BaseModel
        """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            clas_dict = {'BaseModel': BaseModel,
                         'User': User,
                         'State': State,
                         'City': City,
                         'Amenity': Amenity,
                         'Place': Place,
                         'Review': Review}
            new_obj = clas_dict[args]()
            new_obj.save()
            print('{}'.format(new_obj.id))

    def do_show(self, args):
        """
        Prints the string representation on the class name
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            clas_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in clas_dict.keys():
                print("** no instance found **")
            else:
                print(clas_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Deletes an instance"""
        args = args.split()
        clas_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in clas_dict.keys():
                print("** no instance found **")
            else:
                del clas_dict[key]
                clas_dict.storage.save()

    def do_all(self, args):
        """  Prints all string representation """
        args = args.split()
        if args[0] in HBNBCommand.__classes:
            str_list = []
            objs = storage.all()
            for instance in objs.values():
                str_list.append(instance.__str__())
            print(str_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance"""
        args = args.split()
        clas_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in clas_dict.keys():
            print("** no instance found **")
        else:
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                key = args[0] + "." + args[1]
                setattr(clas_dict[key], args[2], args[3])
                clas_dict[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
