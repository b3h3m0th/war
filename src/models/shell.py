from cmd import Cmd


class Shell(Cmd):
    intro = "Welcome to the war shell. Type help or ? to list commands.\n"
    prompt = "(war) "

    def __init__(self) -> None:
        super().__init__()
        self.intro = self.print_menu()

    def print_menu(self) -> None:
        print()
        print("┌──────────────────────────────────┐")
        print("│            WAR - Menu            │")
        print("├──────────────────────────────────┤")
        print("│                                  │")
        print("│  (new) Start new game            │")
        print("│  (quit) Quit                     │")
        print("│                                  │")
        print("├──────────[Danger zone]───────────┤")
        print("│                                  │")
        print("│  (stats) Statistics              │")
        print("│                                  │")
        print("└──────────────────────────────────┘")

    def do_new(self, arg) -> None:
        """Start a new game"""
        print("New game starting")

    def do_stats(self, arg) -> None:
        "Show statistics"
        print("Statistics")

    def do_quit(self, arg) -> bool:
        "Quit"
        print("Thank you for playing war")
        return True


if __name__ == "__main__":
    Shell().cmdloop()
