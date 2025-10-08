from models.deck import Deck
from models.player import Player
from enums.variant import Variant


class Game:
    players: list[Player]
    deck: Deck
    variant: Variant

    def __init__(self, players: list[Player], variant: Variant) -> None:
        self.players = players
        self.variant = variant
        self.deck = Deck() 
        self.deck.shuffle()
