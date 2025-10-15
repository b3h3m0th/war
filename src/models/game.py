from models.deck import Deck
from models.player import Player
from enums.variant import Variant

from prompt_toolkit.shortcuts import choice


class Game:
    def __init__(
        self, players: list[Player] = [], variant: Variant = Variant.NoJoker
    ) -> None:
        self.players = players
        self.variant = variant
        self.deck = Deck()

    def pvc(self, arg) -> None:
        """
        Runs the game in Player vs Computer mode
        """

        print("Player vs Computer mode")
        player = Player(name=input("Enter your name: ").strip())
        computer = Player(name="Computer")
        self.players = [player, computer]
        print(f"Players: {self.players[0].name} vs {self.players[1].name}")

    def pvp(self, arg) -> None:
        """
        Runs the game in Player vs Player mode
        """

        print("Player vs Player mode")
        player1 = Player(name=input("Enter name for Player 1: ").strip())
        player2 = Player(name=input("Enter name for Player 2: ").strip())
        self.players = [player1, player2]
        print(f"Players: {self.players[0].name} vs {self.players[1].name}")

    def start(self) -> None:
        """
        Starts the game
        """

        player_choice = choice(
            message="Choose a gamemode",
            options=[
                ("pvc", "Player vs Computer"),
                ("pvp", "Player vs Player"),
            ],
            default="pvc",
        )

        if player_choice == "pvc":
            self.pvc(self)
        elif player_choice == "pvp":
            self.pvp(self)

        self.deck.shuffle()
