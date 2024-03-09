#!/usr/bin/python3
import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
