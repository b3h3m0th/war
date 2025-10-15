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
        return (
            isinstance(other, Turn)
            and self.player == other.player
            and self.card == other.card
        )

    def __hash__(self):
        """
        Returns a hash value for Turn based on the player
        and card
        """

        return hash((self.player, self.card))
