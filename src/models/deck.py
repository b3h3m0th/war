from __future__ import annotations

from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    cards: list[Card] = []

    def __init__(self, cards=[]):
        self.cards = cards

    def get_new_deck() -> Deck:
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(suit, rank))

        return Deck(cards)
