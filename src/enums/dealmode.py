from __future__ import annotations
from enum import Enum


class DealMode(Enum):
    INSTANT: str = "INSTANT"
    SEQUENTIAL: str = "SEQUENTIAL"

    def to_dict(self: DealMode) -> dict:
        """
        Converts a DealMode into a dictionary that can be stringified into json
        """

        return {"value": self.value}

    @classmethod
    def from_dict(cls: DealMode, data: dict) -> DealMode:
        """
        Returns a DealMode based on a json dictionary
        """

        return cls(data["value"])
