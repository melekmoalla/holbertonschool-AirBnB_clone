#!/usr/bin/python3
"""
    This is the console module
"""
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Do nothing on empty line"""
        if (len(arg) == 0):
            print("** class name missing **")
            return
        elif arg != "BaseModel" and arg != 'FileStorage':
            print("** class doesn't exist **")
            return
        else:
            m = BaseModel()
            m.save()
            print(m.id)

    def do_show(self, arg):
        args = arg.split()
        if (len(arg) == 0):
            print("** class name missing **")
        elif args[0] != "BaseModel" and args[0] != 'FileStorage':
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return
        else:
            z = 0
            dic = {}
            all_objs = storage.all()
            for i in all_objs:
                s = i.split()
                p = s[0].split(".")
                dic[p[1]] = s
            for b in dic:
                if (b == args[1]):
                    print(all_objs[dic[b][0]])
                    z = 1
            if (z == 0):
                print("** no instance found **")
            return

    def do_destroy(self, arg):
        args = arg.split()
        if (len(arg) == 0):
            print("** class name missing **")
        elif args[0] != "BaseModel" and args[0] != 'FileStorage':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            z = 0
            dic = {}
            all_obj = storage.all()
            for i in all_obj:
                s = i.split()
                p = s[0].split(".")
                dic[p[1]] = s
            for b in dic:
                if (b == args[1]):
                    del all_obj[dic[b][0]]
                    storage.save()
                    z = 1
            if (z == 0):
                print("** no instance found **")
            return

    def do_all(self, arg):
        args = arg.split()
        if (len(arg) == 0):
            m = []
            a = storage.all()
            for value in a:
                m.append(str(a[value]))
            print(m)
            return
        elif args[0] != "BaseModel" and args[0] != 'FileStorage':
            print("** class doesn't exist **")
            return
        else:
            m = []
            a = storage.all()
            for value in a:
                m.append(str(a[value]))
            print(m)

    def do_update(self, arg):
        args = arg.split()
        if (len(arg) == 0):
            print("** class name missing **")
            return
        elif args[0] != "BaseModel" and args[0] != 'FileStorage':
            print("** class doesn't exist **")
            return
        elif (len(args) == 1):
            print("** instance id missing **")
            return
        elif (len(args) == 2):
            print("** attribute name missing **")
            return
        elif (len(args) == 3):
            print("** value missing **")
            return
        else:
            z = 0
            a = storage.all()
            p = {}
            for i in a:
                s = i.split()
                o = s[0].split(".")
                p[o[1]] = s
            for e in p:
                if (e == args[1]):
                    z = 1
            if z == 0:
                print("** no instance found **")
                return
        args = arg.split()
        y = storage.all()
        name_class = args[0]
        id_class = args[1]
        key = name_class+"."+id_class
        value = y[key].__dict__
        args_name = args[3].split("\"")
        value[args[2]] = str(args_name[1])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
