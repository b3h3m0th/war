from enums.suit import Suit
from enums.rank import Rank

SUIT_STRINGS = {
    Suit.Spades: "♠",
    Suit.Hearts: "♥",
    Suit.Clubs: "♣",
    Suit.Diamonds: "♦",
}

RANK_STRINGS = {
    Rank.Ace: "A",
    Rank.King: "K",
    Rank.Queen: "Q",
    Rank.Jack: "J",
}

class Card:
    suit: Suit
    rank: Rank

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        suit_string = SUIT_STRINGS.get(self.suit);
        .get(self.rank, str(self.rank.value))

        return f"{rank_str}{ran[self.suit]}"

    def __repr__(self) -> str:
        return f"Card({self.rank.name} of {self.suit.name})"
