from __future__ import annotations
from enum import Enum


class Variant(Enum):
    JokerHighest: str = "JokerHighest"
    JokerInstantWar: str = "JokerInstantWar"
    JokerPenalty: str = "JokerPenalty"
    NoJoker: str = "NoJoker"

    def to_dict(self) -> dict:
        """
        Converts a Variant into a dictionary that can be stringified into json
        """

        return {
            "value": self.value,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Variant:
        """
        Returns a Variant based on a json dictionary
        """

        return cls(data["value"])
