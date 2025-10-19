from __future__ import annotations
from models.player import Player
from models.card import Card


class Turn:
    def __init__(self: Turn, player: Player, card: Card) -> None:
        """
        Instantiates a new Turn with a given Player and a given Card
        """

        self.player = player
        self.card = card

    def __str__(self: Turn) -> str:
        """
        Displays a Turn as a string with Card and Player
        """

        return f"{self.player}: {self.card}"

    def __eq__(self: Turn, other: Turn) -> bool:
        """
        Checks whether a Turn is equal to another Turn
        Turns are considered equal if their player and card are equal
        """

        return (
            isinstance(other, Turn)
            and self.player == other.player
            and self.card == other.card
        )

    def __hash__(self: Turn) -> int:
        """
        Returns a hash based on the Player and Card
        """

        return hash((self.player, self.card))

    def to_dict(self: Turn) -> dict:
        """
        Converts a Turn into a dictionary that can be stringified into json
        """

        return {"player": self.player.to_dict(), "card": self.card.to_dict()}

    @classmethod
    def from_dict(cls: Turn, data: dict) -> Turn:
        """
        Creates and returns a Turn based on a json dictionary
        """

        return cls(
            Player.from_dict(data["player"]), Card.from_dict(data["card"])
        )
