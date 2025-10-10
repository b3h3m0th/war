from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns):
        self.turns = turns

    def get_winning_round(self) -> Turn:
        if self.turns[0].card > self.turns[1]:
            return self.turns(0)
        elif self.turns[1].card > self.turns[0]:
            return self.turns(1)
