from enums.suit import Suit
from enums.rank import Rank


class Card:
    suit: Suit
    rank: Rank

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        suit_str = {
            Suit.Spades: "♠",
            Suit.Hearts: "♥",
            Suit.Clubs: "♣",
            Suit.Diamonds: "♦",
        }
        rank_str = {
            Rank.Ace: "A",
            Rank.King: "K",
            Rank.Queen: "Q",
            Rank.Jack: "J",
        }.get(self.rank, str(self.rank.value))

        return f"{rank_str}{SUIT_EMOJIS[self.suit]}"

    def __repr__(self) -> str:
        return f"Card({self.rank.name} of {self.suit.name})"
