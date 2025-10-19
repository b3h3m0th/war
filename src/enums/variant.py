from __future__ import annotations
from enum import Enum


class Variant(Enum):
    NO_JOKERS: str = "NO_JOKERS"
    JOKERS_HIGHEST: str = "JOKERS_HIGHEST"

    def to_dict(self: Variant) -> dict:
        """
        Converts a Variant into a dictionary that can be stringified into json
        """

        return {"value": self.value}

    @classmethod
    def from_dict(cls: Variant, data: dict) -> Variant:
        """
        Returns a Variant based on a json dictionary
        """

        return cls(data["value"])
