from __future__ import annotations


class Player:
    def __init__(self, name: str) -> None:
        """
        Instantiates a new Card with a given name
        """

        self.name = name

    def to_dict(self) -> dict:
        """
        Converts a Player into a dictionary that can be stringified into json
        """

        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Player:
        """
        Creates and returns a Player based on a json dictionary
        """

        return cls(data["name"])
