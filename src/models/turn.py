from models.player import Player
from models.card import Card


class Turn:
    player: Player
    card: Card

    def __init__(self, player, card) -> None:
        self.player = player
        self.card = card
