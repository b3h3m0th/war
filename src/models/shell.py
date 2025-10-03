from cmd import Cmd


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
    intro = "Welcome to the war shell. Type help or ? to list commands.\n"
    prompt = "(war) "
    file = None

    def do_exit(self, arg):
        "Exit shell"
        print("Thank you for using shell")
        self.close()
        return True

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
