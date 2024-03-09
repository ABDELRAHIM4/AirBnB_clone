"""Write a program called console.py that contains the entry point of the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """class definition must be: class HBNBCommand(cmd.Cmd)"""
    def do_EOF(self,arg):
        """EOF to exit the program"""
        return True
    def do_quit(self,arg):
        """Quit command to exit the program"""
        return True
    def do_emptyline(self,arg):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
        self.resetbuffer(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
