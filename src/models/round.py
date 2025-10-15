from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns):
        """
        Instantiates a new Round object which consists of a list of Turns
        """

        self.turns = turns

    def get_winning_turn(self) -> Turn:
        """
        Compares turns and returns the winner. If there are no turns or
        the turns are equal it returns None
        """

        if not self.turns:
            return None

        counter = 0

        while True:
            winner = self.turns[counter]
            if self.turns[counter + 1].card.rank == winner.card.rank:
                counter += 2
                if counter >= len(self.turns) - 1:
                    return None
                continue
            if self.turns[counter + 1].card.rank > winner.card.rank:
                winner = self.turns[counter + 1]
                break
            else:
                break

        return winner

    def __eq__(self, other) -> bool:
        """
        A Round object is equal if the compared turns have equal values
        """

        return isinstance(other, Round) and self.turns == other.turns

    def __hash__(self) -> int:
        """
        Returns a hash value based on turns
        """

        return hash((self.turns))
