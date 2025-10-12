from cmd import Cmd
from models.game import Game


class Shell(Cmd):
    intro: str = "Welcome to the war shell. Type help or ? to list commands.\n"
    prompt: str = "(war) "
    game: Game

    def __init__(self) -> None:
        super().__init__()
        self.intro = self.print_menu()

    def print_menu(self) -> None:
        print()
        print("┌──────────────────────────────────┐")
        print("│            WAR - Menu            │")
        print("├──────────────────────────────────┤")
        print("│                                  │")
        print("│  (new)   Start new game          │")
        print("│  (help)  List commands           │")
        print("│  (stats) Statistics              │")
        print("│  (quit)  Quit                    │")
        print("│                                  │")
        print("├────────────[Options]─────────────┤")
        print("│                                  │")
        print("│  TBA                             │")
        print("│                                  │")
        print("└──────────────────────────────────┘")

    def do_new(self, arg) -> None:
        """Start a new game"""
        self.game = Game(players=[], variant=None)
        self.game.start()

    def do_quit(self, arg) -> bool:
        "Quit"
        print("Thank you for playing war")
        return True

    def default(self, line):
        print(
            f'Unknown option: "{line}". '
            "Use help or ? to get a list of all options."
        )


if __name__ == "__main__":
    Shell().cmdloop()
