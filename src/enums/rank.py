from __future__ import annotations
from enum import Enum


class Rank(Enum):
    Two: int = 2
    Three: int = 3
    Four: int = 4
    Five: int = 5
    Six: int = 6
    Seven: int = 7
    Eight: int = 8
    Nine: int = 9
    Ten: int = 10
    Jack: int = 11
    Queen: int = 12
    King: int = 13
    Ace: int = 14

    def to_dict(self) -> dict:
        """
        Converts a Rank into a dictionary that can be stringified into json
        """

        return {"value": self.value}

    @classmethod
    def from_dict(cls, data: dict) -> Rank:
        """
        Returns a Rank based on a json dictionary
        """

        return cls(data["value"])
