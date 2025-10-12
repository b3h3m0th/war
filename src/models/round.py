from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns=[]):
        self.turns = turns

    def get_winning_turn(self) -> Turn | None:
        """
        Returns the turn of the round with the highest played card by rank.
        Returns None if the round has no turns or there is a tie.
        """

        winning_turn: Turn | None = None

        for turn in self.turns:
            if not winning_turn or turn.card.rank > winning_turn.card.rank:
                winning_turn = turn
            elif turn.card.rank == winning_turn.rank:
                winning_turn = None

        return winning_turn
