from __future__ import annotations

from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    cards: list[Card] = []

    def __init__(self, cards: list[Card] = []) -> None:
            self.cards = cards if cards else self.get_new_sorted_cards()

    def get_new_sorted_cards() -> list[Card]:
        return [Card(suit, rank) for suit in Suit for rank in Rank]
    
    def shuffle() -> None:
         

