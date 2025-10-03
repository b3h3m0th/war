from __future__ import annotations
import random

from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    cards: list[Card] = []

    def __init__(self, cards: list[Card] = []) -> None:
        self.cards = cards if cards else self.get_new_sorted_cards()

    def get_new_sorted_cards() -> list[Card]:
        new_deck_order_suits = [Suit.Spades, Suit.Diamonds, Suit.Clubs, Suit.Hearts]
        new_deck_order_ranks = [Rank.Ace, rank for rank in Rank if rank is not Rank.Ace]

        return [Card(suit, rank) for suit in new_deck_order_suits for rank in new_deck_order_ranks]

    def shuffle(self, cards: list[Card]) -> list[Card]:
        if not cards:
            cards = self.cards

        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]

        return cards
