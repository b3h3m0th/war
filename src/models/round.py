from models.turn import Turn


class Round:
    turns: list[Turn]

    def __init__(self, turns):
        self.turns = turns

    def get_winning_round(self) -> Turn:
        if not self.turns:
            return None
        
        counter = 0
        winning_card = self.turns[counter].card
        
        while True:
            if self.turns[counter + 1].card == winning_card:
                counter += 2
                if counter >= len(self.turns) - 1:
                    return None
                continue
            if self.turns[counter + 1].card > winning_card:
                winning_card = self.turns[counter + 1].card
                break
            
        return winning_card


        

