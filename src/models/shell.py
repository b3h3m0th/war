from cmd import Cmd
from turtle import *


class Menu:
    def print_menu():
        print()
        print("┌──────────────────────────────────┐")
        print("│               Menu               │")
        print("├──────────────────────────────────┤")
        print("│                                  │")
        print("│  (R)egister points               │")
        print("│  (S)how grades                   │")
        print("│  (E)xit                          │")
        print("│                                  │")
        print("├──────────[Danger zone]───────────┤")
        print("│                                  │")
        print("│  (Reset) points                  │")
        print("│                                  │")
        print("└──────────────────────────────────┘")


class Shell(Cmd):
    intro = "Welcome to the turtle shell.   Type help or ? to list commands.\n"
    prompt = "(turtle) "
    file = None

    def do_undo(self, arg):
        "Undo (repeatedly) the last turtle action(s):  UNDO"

    def do_reset(self, arg):
        "Clear the screen and return turtle to center:  RESET"
        reset()

    def do_stop(self, arg):
        "Stop recording, close the turtle window, and exit:  BYE"
        print("Thank you for using")
        self.close()
        return True

    def do_greet(self, arg):
        """Greet someone:  greet <name>"""
        if arg:
            print(f"Hello, {arg}!")
        else:
            print("Hello!")

    def do_add(self, arg):
        """Add two numbers:  add 4 5"""
        try:
            a, b = map(float, arg.split())
            print(a + b)
        except ValueError:
            print("Please provide two numbers.")

    # Shortcut for exit
    def do_EOF(self, arg):
        "Shortcut for exit"
        return self.do_exit(arg)

    # ----- record and playback -----
    def do_record(self, arg):
        "Save future commands to filename:  RECORD rose.cmd"
        self.file = open(arg, "w")

    def do_playback(self, arg):
        "Playback commands from a file:  PLAYBACK rose.cmd"
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and "playback" not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    "Convert a series of zero or more numbers to an argument tuple"
    return tuple(map(int, arg.split()))


if __name__ == "__main__":
    Shell().cmdloop()
