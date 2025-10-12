from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns=[]):
        """
        Instantiates a new Round
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
