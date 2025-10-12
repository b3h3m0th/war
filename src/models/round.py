from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns = []):
        self.turns = turns

    def get_winning_round(self) -> Turn:
