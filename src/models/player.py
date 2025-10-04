import json
from annotations import __future__

class Player:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: ) -> Player:
        return cls(data["name"], data["age"], address)
