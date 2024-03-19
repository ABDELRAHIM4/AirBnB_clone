#!/usr/bin/python3
"""Write a program called console.py"""
import cmd
import sys
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
"""Write a program called console.py that contains the entry point of the command interprete"""
class HBNBCommand(cmd.Cmd):
    """class definition must be: class HBNBCommand(cmd.Cmd)"""
    prompt = "(hbnb)"
    def do_EOF(self,arg):
        """EOF to exit the program"""
        return True
    def do_quit(self,arg):
        """Quit command to exit the program"""
        return True
    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
    def do_create(self,arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        

        if len(args) < 1:
            print ("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
            else:
                st = eval(class_name)()
                st.save()
                storage.new(st)
                print(st.id)
                class_name = arg
                count = storage.count(class_name)
                print(count)
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        obj = {}
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            n_id = args[1]

            if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                print("** class doesn't exist **")
            else:
                    obj = storage.all()
                    if obj is not  None:
                                for key, value in obj.items():
                                    if key.startswith(class_name) and value.id == n_id:
                                        print(f"{value}")
                                        break
                                    else:
                                        print("** no instance found **")
                    else:
                        print("** no instance found **")

    def do_destroy(self,arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(args) < 2 & len(args) > 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")
    def do_all(self, arg):
        """Prints all string representation of all instances of a class"""
        args = arg.split('.')
        if not args:
            print("** class name required **")
        else:
            class_name = args[0]
            objs = storage.all()
            my_list = []
            if class_name in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                if objs:
                    for value in objs.values():
                            my_list.append(str(value))
                    print(my_list)
                else:
                    print("** no instances found **")
            elif class_name == "User":
                if objs:
                    for value in objs.values():
                        if type(value).__name__ == "User":
                            my_list.append(repr(value))
                    print(my_list)
            elif args[1] == 'all()':
                class_name = args[0]
                if class_name in storage.classes():
                    objs = storage.all(class_name)
                    for obj in objs.values():
                        print(obj)
                else:
                    print("** class doesn't exist **")
            else:
                     print("** class doesn't exist **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
