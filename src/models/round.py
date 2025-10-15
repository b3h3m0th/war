from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns):
        self.turns = turns

    def get_winning_turn(self) -> Turn:
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
        return isinstance(other, Round) and self.turns == other.turns
