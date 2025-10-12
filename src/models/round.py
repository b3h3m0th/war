from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns=[]):
        """
        Instantiates a new Round with a given list of turns.
        """

        self.turns = turns

    def get_winning_turns(self) -> list[Turn]:
        """
        Returns a list of turns with the highest cards by rank.
        Returns a a list of mulitple turns in case ofa tie.
        Returns an empty list if there are no turns.
        """

        if not self.turns:
            return []

        max_rank = max(turn.card.rank.value for turn in self.turns)
        return [
            turn for turn in self.turns if turn.card.rank.value == max_rank
        ]

    def __eq__(self, other) -> bool:
        """
        Checks whether a Round is equal to another Round
        """

        return isinstance(other, Round) and self.turns == other.turns

    def __hash__(self) -> int:
        """
        Computes a hash of a Round based on its turns
        """

        return hash(turn for turn in self.turns)

    def to_dict(self) -> dict:
        """
        Converts a Round into a dictionary that can be stringified into json
        """

        return {
            "turns": [turn.to_dict() for turn in self.turns],
        }

    @classmethod
    def from_dict(cls, data: dict) -> Turn:
        """
        Creates and returns a Round based on a json dictionary
        """

        return cls([Turn.from_dict(turn) for turn in data["turns"]])
