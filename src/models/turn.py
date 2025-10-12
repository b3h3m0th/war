from models.player import Player
from models.card import Card


class Turn:
    def __init__(self, player: Player, card: Card) -> None:
        """
        Instantiates a new Turn with a given Player and a given Card
        """

        self.player = player
        self.card = card
