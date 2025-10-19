from __future__ import annotations
from enum import Enum


class Matchup(Enum):
    PLAYER: str = "PLAYER"
    COMPUTER: str = "COMPUTER"

    def to_dict(self: Matchup) -> dict:
        """
        Converts a Matchup into a dictionary that can be stringified into json
        """

        return {"value": self.value}

    @classmethod
    def from_dict(cls: Matchup, data: dict) -> Matchup:
        """
        Returns a Matchup based on a json dictionary
        """

        return cls(data["value"])
