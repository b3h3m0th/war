from models.player import Player
from models.card import Card


class Turn:
    def __init__(self, player: Player, card: Card) -> None:
        self.player = player
        self.card = card
