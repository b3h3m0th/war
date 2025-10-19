from __future__ import annotations
from cmd import Cmd
from models.game import Game
from models.player import Player
from utils.serializer import Serializer


from pathlib import Path
from prompt_toolkit.shortcuts import choice


class Shell(Cmd):
    intro: str = "Welcome to the war shell. Type help or ? to list commands.\n"
    prompt: str = "(war) "

    game: Game
    games_path: Path = Path("./data/games")

    def __init__(self: Shell) -> None:
        """
        When instantiated calls the constructor of
        super class Cmd. Prints the menu for the current game.
        """

        super().__init__()
        self.intro = self.print_menu()

    def print_menu(self: Shell) -> None:
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
        print("│  (chng)  Change player name      │")
        print("│  (help)  List commands           │")
        print("│  (quit)  Quit                    │")
        print("│                                  │")
        print("└──────────────────────────────────┘")

    def do_rules(self: Shell, arg: str) -> None:
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

    def do_menu(self: Shell, arg: str) -> None:
        """
        Shows the menu if the user wants the menu again
        """

        self.print_menu()

    def do_new(self: Shell, arg: str) -> None:
        """
        Start a new game
        """

        self.game = Game()

        previous_games: list[Game] = self.get_previous_games()
        taken_player_names: list[str] = [
            player.name for game in previous_games for player in game.players
        ]

        self.game.start(taken_player_names)

        save_game: bool = choice(
            message="Do you want to save this game",
            options=[(True, "Yes"), (False, "No")],
            default=False,
        )

        if save_game:
            Serializer.save(
                self.game, self.games_path / f"{self.game.name}.json"
            )

    def do_log(self: Shell, arg: str) -> None:
        for game in self.get_previous_games():
            game.print_results()

    def do_chng(self: Shell, arg: str) -> None:
        """
        Change a players name
        """

        games: list[Game] = self.get_previous_games()
        distinct_players: list[Player] = []

        for game in games:
            for player in game.players:
                if player not in distinct_players and not player.isNpc:
                    distinct_players.append(player)

        selected_player: Player = choice(
            message="Which player name do you want to change?",
            options=[
                (Player(player.name, player.isNpc), player.name)
                for player in distinct_players
            ],
        )
        new_name: str = input(f"Select a new name for {selected_player}: ")

        for game in games:
            for player in game.players:
                if player == selected_player:
                    player.name = new_name

            for round in game.rounds:
                for turn in round.turns:
                    if turn.player == selected_player:
                        turn.player.name = new_name

            Serializer.save(game, self.games_path / f"{game.name}.json")

        print(f'Updated player "{selected_player.name}" to "{new_name}" ')

    def do_quit(self: Shell, arg: str) -> bool:
        """
        Quit the game
        """

        print("Thank you for playing war")
        return True

    def default(self: Shell, line: str) -> None:
        """
        Default case for unknown command
        """

        print(
            f'Unknown option: "{line}". '
            'Use "help" or "?"" to get a list of all options '
            'or use "menu" to get the initial start screen menu.'
        )

    def get_previous_games(self) -> list[Game]:
        return [
            Serializer.load(Game, file)
            for file in self.games_path.glob("*.json")
        ]


if __name__ == "__main__":
    Shell().cmdloop()
