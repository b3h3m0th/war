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
        print("│  (rules) Shows game rules        │")
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
        """Quit the game"""
        "Quit"
        print("Thank you for playing war")
        return True

    def default(self, line):
        """Default case for unknown command"""
        print(
            f'Unknown option: "{line}". '
            "Use help or ? to get a list of all options."
        )

    def do_rules(self, arg) -> None:
        """Shows the rules of the game"""
        print(
            "This is our implementation of the casino "
            "war game.The rules are slightly different"
            " to the casino war game as we are not "
            "including betting for this game. You start"
            " the game by choosing which game variant you"
            " want (to be implemented). You then choose if"
            " you will start a new game or load a previous"
            " one. You then choose if you want to play vs"
            " a real player or a computer. If you chose"
            " the basic war game each player will get"
            " handed a card by a dealer(a method). If"
            " your card is higher ranked than the other "
            "player you get awarded a point, if it a "
            "draw you go to war and a card is drawn "
            "again for each player. Whoever has the "
            "highest card gets a point or if it is a "
            "draw again the process is repeated until "
            "a player can get a awarded a point. This"
            " counts as 1 round. After each round you"
            " will get asked if you want to a card to"
            " be drawn. If you choose not to then you"
            " will have a choice to save the game and"
            " quit(to be implemented) or just quit"
            " without saving. Once you quit the current"
            " game you will have a choice from the menu"
            " options. (Currently just show stats(not "
            "implemented), show rules, start a new game,"
            " load game, quit, choose variant or game "
            "rules(not implemented))"
        )


if __name__ == "__main__":
    Shell().cmdloop()
