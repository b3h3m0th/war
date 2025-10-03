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

    def do_new_gamge(self, arg):
        "Start a new game"
        print("New game starting")

    def do_statistics(self, arg):
        "Show statistics"
        print("Statistics")

    def do_exit(self, arg):
        "Exit"
        print("Thank you for using war")
        self.close()
        return True


if __name__ == "__main__":
    Shell().cmdloop()
