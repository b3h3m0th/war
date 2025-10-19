from __future__ import annotations
from enums.suit import Suit
from enums.rank import Rank

SUIT_STRINGS = {
    Suit.Spades: "♠",
    Suit.Hearts: "♥",
    Suit.Clubs: "♣",
    Suit.Diamonds: "♦",
}

RANK_STRINGS = {Rank.Ace: "A", Rank.King: "K", Rank.Queen: "Q", Rank.Jack: "J"}


class Card:
    def __init__(self: Card, suit: Suit, rank: Rank) -> None:
        """
        Instantiates a new Card with a given suite and rank
        """

        self.suit: Suit = suit
        self.rank: Rank = rank

    def __str__(self: Card) -> str:
        """
        Displays a card as a string with the according symbol of its suit
        """

        suit_string = SUIT_STRINGS.get(self.suit)
        rank_string = RANK_STRINGS.get(self.rank, str(self.rank.value))

        return f"{rank_string}{suit_string}"

    def __eq__(self: Card, other: Card) -> bool:
        """
        Checks whether a card is equal to another card
        """

        return (
            isinstance(other, Card)
            and self.suit == other.suit
            and self.rank == other.rank
        )

    def __hash__(self: Card) -> int:
        """
        Computes a hash of a card based on its suit and rank
        """

        return hash((self.suit, self.rank))

    def to_dict(self: Card) -> dict:
        """
        Converts a card into a dictionary that can be stringified into json
        """

        return {"suit": self.suit.to_dict(), "rank": self.rank.to_dict()}

    @classmethod
    def from_dict(cls: Card, data: dict) -> Card:
        """
        Creates and returns a card based on a json dictionary
        """

        return cls(Suit.from_dict(data["suit"]), Rank.from_dict(data["rank"]))
