from models.player import Player
from models.card import Card


class Turn:
    def __init__(self, player: Player, card: Card) -> None:
        """
        Instantiates a new Turn with a given Player and a given Card
        """

        self.player = player
        self.card = card

    def __eq__(self, other) -> bool:
        """
        Return True if this Turn is equal to another Turn

        Turn objects are considered equal if they have the same
        values for player and card
        """

        return (
            isinstance(other, Turn)
            and self.player == other.player
            and self.card == other.card
        )
