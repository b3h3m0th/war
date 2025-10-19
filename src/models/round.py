from __future__ import annotations
from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self: Round, turns: list[Turn] = None) -> None:
        """
        Instantiates a new Round with a given list of turns.
        """

        self.turns = turns or []

    def get_winning_turns(self: Round) -> list[Turn]:
        """
        Returns a list of turns with the highest cards by rank.
        Returns a list of multiple turns in case of a tie.
        Returns an empty list if there are no turns.
        """

        counter: int = 0
        max_rank: int = None
        winning_turns: list[Turn] = []

        while counter < len(self.turns):
            current_turn = self.turns[counter]
            current_rank = current_turn.card.rank.value

            if max_rank is None or current_rank > max_rank:
                max_rank = current_rank
                winning_turns = [current_turn]
            elif current_rank == max_rank:
                winning_turns.append(current_turn)

            counter += 1

        return winning_turns

    def __eq__(self: Round, other: Round) -> bool:
        """
        Checks whether a Round is equal to another Round
        Two rounds are equal if the compared turns have equal values
        """

        return isinstance(other, Round) and self.turns == other.turns

    def __hash__(self: Round) -> int:
        """
        Returns a hash based on turns
        """

        return hash(tuple(self.turns))

    def to_dict(self: Round) -> dict:
        """
        Converts a Round into a dictionary that can be stringified into json
        """

        return {"turns": [turn.to_dict() for turn in self.turns]}

    @classmethod
    def from_dict(cls: Round, data: dict) -> Turn:
        """
        Creates and returns a Round based on a json dictionary
        """

        return cls([Turn.from_dict(turn) for turn in data["turns"]])
