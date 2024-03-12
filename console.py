#!/usr/bin/python3
"""Write a program called console.py"""
import cmd
import sys
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
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                st = BaseModel()
                st.save()
                print(st.id)
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            id = args[1]

            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                if getattr(sys.modules[__name__], class_name, None) is not None:
                    obj = storage.__objects
                    if id in storage:
                        obj = storage.all()
                        print(obj)
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
        args = arg.split()
        if not args:
            print("** class name required **")
        else:
            class_name = args[0]
            objs = storage.all()
            my_list = []
            if class_name == "BaseModel":
                if objs != None:
                    for value in objs.values():
                            my_list.append(repr(value))
                    print(my_list)
                else:
                    print("** no instances found **")
            else:
                print("** class doesn't exist **")
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
