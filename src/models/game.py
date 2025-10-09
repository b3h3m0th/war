from models.deck import Deck
from models.player import Player
from enums.variant import Variant


class Game:
    def __init__(
        self, players: list[Player] = [], variant: Variant = Variant.NoJoker
    ) -> None:
        self.players = players
        self.variant = variant
        self.deck = Deck()
