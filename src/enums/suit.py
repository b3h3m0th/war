from __future__ import annotations
from enum import Enum


class Suit(Enum):
    Spades: str = "Spades"
    Hearts: str = "Hearts"
    Clubs: str = "Clubs"
    Diamonds: str = "Diamonds"

    def to_dict(self) -> dict:
        """
        Converts a Suit into a dictionary that can be stringified into json
        """

        return {"value": self.value}

    @classmethod
    def from_dict(cls, data: dict) -> Suit:
        """
        Returns a Suit based on a json dictionary
        """

        return cls(data["value"])
