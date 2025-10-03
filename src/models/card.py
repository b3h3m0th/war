from enums.suit import Suit
from enums.rank import Rank


class Card:
    suit: Suit
    rank: Rank

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank
