from __future__ import annotations


class Player:
    def __init__(self: Player, name: str, isNpc: bool = False) -> None:
        """
        Instantiates a new Card with a given name
        """

        self.name = name
        self.isNpc = isNpc

    def __str__(self: Player) -> str:
        """
        Displays a Player as a string
        """

        return f"{self.name}"

    def to_dict(self: Player) -> dict:
        """
        Converts a Player into a dictionary that can be stringified into json
        """

        return {"name": self.name, "isNpc": self.isNpc}

    def __eq__(self: Player, other: Player) -> bool:
        return (
            isinstance(other, Player)
            and self.name == other.name
            and self.isNpc == other.isNpc
        )

    def __hash__(self: Player) -> int:
        return hash((self.name, self.isNpc))

    @classmethod
    def from_dict(cls: Player, data: dict) -> Player:
        """
        Creates and returns a Player based on a json dictionary
        """

        return cls(data["name"], data["isNpc"])
