from models.deck import Deck
from models.player import Player
from enums.variant import Variant


class Game:
    players: list[Player]
    deck: Deck
    variant: Variant

    def __init__(self, players: list[Player], variant: Variant) -> None:
        self.players = players
        self.variant = variant
        self.deck = Deck()
        self.deck.shuffle(cards=[])

    def do_stats(self, arg) -> None:
        "Show statistics"
        print("Statistics")

    def do_pvc(self, arg) -> None:
        "Player vs Computer"
        print("Player vs Computer mode")
        player = Player(name=input("Enter your name: ").strip())
        computer = Player(name="Computer")
        self.players = [player, computer]
        print(f"Players: {self.players[0].name} vs {self.players[1].name}")

    def do_pvp(self, arg) -> None:
        "Player vs Player"
        print("Player vs Player mode")
        player1 = Player(name=input("Enter name for Player 1: ").strip())
        player2 = Player(name=input("Enter name for Player 2: ").strip())
        self.players = [player1, player2]
        print(f"Players: {self.players[0].name} vs {self.players[1].name}")

    def start(self) -> None:
        print("Starting the game...")
        print(
            "Would you like to play Player vs "
            "Computer (pvc) or Player vs Player (pvp)?"
        )
        player_choice = input().strip().lower()
        while (player_choice!= "pvc" or player_choice !="pvp"):
            if player_choice == "pvc":
                self.do_pvc(self)
                break
            elif player_choice == "pvp":
                self.do_pvp(self)
                break
            else:
                print(f"Incorrect input try again.Would you like to play Player vs "
            "Computer (pvc) or Player vs Player (pvp)?")
                player_choice = input().strip().lower()


        self.deck.shuffle(None)
