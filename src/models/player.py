from __future__ import annotations


class Player:
    def __init__(self, name: str, isNPC: bool) -> None:
        self.name = name
        self.isNPC = bool
        if (self.isNPC):
            self.name = "Computer"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "isNPC": self.isNPC
        }

    @classmethod
    def from_dict(cls, data: dict) -> Player:
        return cls(data["name"])
