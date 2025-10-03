from cmd import Cmd


class Menu:
    def print_menu():
        print()
        print("┌──────────────────────────────────┐")
        print("│               WAR - Menu         │")
        print("├──────────────────────────────────┤")
        print("│                                  │")
        print("│  (new) Start new game            │")
        print("│  (stats) Statistics              │")
        print("│  (quit) Quit                     │")
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

    def do_new(self, arg):
        "Start a new game"
        print("New game starting")

    def do_stats(self, arg):
        "Show statistics"
        print("Statistics")

    def do_quit(self, arg):
        "Quit"
        print("Thank you for using war")
        return True


if __name__ == "__main__":
    Shell().cmdloop()
