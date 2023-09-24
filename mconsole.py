#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
import cmd
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it 
            (to the JSON file) and prints the id"""
        if arg == '' or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[arg]()
            b.save
            print(b.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()    
