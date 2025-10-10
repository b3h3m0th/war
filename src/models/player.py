from __future__ import annotations


class Player:
    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Player:
        return cls(data["name"])
