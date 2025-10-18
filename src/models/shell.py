from cmd import Cmd
from models.game import Game
from utils.serializer import Serializer


from pathlib import Path
from prompt_toolkit.shortcuts import choice


class Shell(Cmd):
    intro: str = "Welcome to the war shell. Type help or ? to list commands.\n"
    prompt: str = "(war) "

    game: Game
    games_path: Path = Path("./data/games")

    def __init__(self) -> None:
        """
        Constructor: When instantiated calls the constructor of super class Cmd.
        Prints the menu for the current game.
        """
        
        super().__init__()
        self.intro = self.print_menu()

    def print_menu(self) -> None:
        """
        Prints the menu on game launch
        """

        print()
        print("┌──────────────────────────────────┐")
        print("│            WAR - Menu            │")
        print("├──────────────────────────────────┤")
        print("│                                  │")
        print("│  (rules) Shows game rules        │")
        print("│  (menu)  Shows the menu          │")
        print("│  (new)   Start new game          │")
        print("│  (log)   Game history            │")
        print("│  (help)  List commands           │")
        print("│  (quit)  Quit                    │")
        print("│                                  │")
        print("└──────────────────────────────────┘")

    def do_menu(self, arg) -> None:
        """
        Shows the menu if the user wants the menu again
        """

        self.print_menu()

    def do_new(self, arg) -> None:
        """
        Start a new game
        """

        self.game = Game()
        self.game.start()

        save_game = choice(
            message="Do you want to save this game",
            options=[(True, "Yes"), (False, "No")],
            default=False,
        )

        if save_game:
            Serializer.save(
                self.game, self.games_path / f"{self.game.name}.json"
            )

    def do_log(self, arg) -> None:
        """
        Loads a game and prints the results of that game
        """
        for json_file in self.games_path.glob("*.json"):
            game = Serializer.load(Game, json_file)
            game.print_results()

        print()

    def do_rules(self, arg) -> None:
        """
        Shows the rules of the game.
        """

        print(
            "Welcome to our version of Casino War!\n\n"
            "The rules are slightly different from the "
            "casino version, as this game does not include "
            "betting.\n\n"
            "At the start, you choose which game variant you "
            "want to play (to be implemented). You then choose "
            "whether to start a new game or load a previous one, "
            "and whether to play against \n another player or the "
            "computer.\n\n"
            "In the basic War game, each player is dealt a card "
            "by the dealer (a method). If your card ranks higher "
            "than your opponent's, you earn one point. If the cards "
            "tie, you go to war and both players \n draw again until "
            "one player wins the round.\n\n"
            "After each round, you will be asked if you want to draw "
            "another card. If you choose not to, you can save the game "
            "and quit (to be implemented) or quit without saving.\n\n"
            "Once you exit the current game, you will return to the "
            "main menu, where you can choose from the following options:\n"
            " - Show stats (not yet implemented)\n"
            " - Show rules\n"
            " - Start a new game\n"
            " - Load a saved game\n"
            " - Quit\n"
            " - Choose variant or game rules (not yet implemented)\n"
        )

    def do_quit(self, arg) -> bool:
        """
        Quit the game
        """

        print("Thank you for playing war")
        return True

    def default(self, line):
        """
        Default case for unknown command
        """

        print(
            f'Unknown option: "{line}". '
            'Use "help" or "?"" to get a list of all options '
            'or use "menu" to get the initial start screen menu.'
        )


if __name__ == "__main__":
    Shell().cmdloop()
