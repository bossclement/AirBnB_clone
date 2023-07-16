#!/usr/bin/python3
"""
This module works like a commmand prompt (CMD)
to interact with users.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from Cmd
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quits the program
        """
        return True

    def do_EOF(self, line):
        """
        Quits the program upon receiving EOF signal
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
