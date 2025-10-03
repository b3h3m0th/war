from __future__ import annotations
import random
from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    cards: list[Card] = []
    new_deck_order_suits = [
        Suit.Spades,
        Suit.Diamonds,
        Suit.Clubs,
        Suit.Hearts,
    ]

    def __init__(self, cards: list[Card] = []) -> None:
        self.cards = cards if cards else self.get_new_deck_order_cards()

    def get_new_deck_order_cards(self) -> list[Card]:
        ace_to_king = [Rank.Ace] + [
            rank for rank in Rank if rank is not Rank.Ace
        ]
        king_to_ace = list(reversed(ace_to_king))

        return [
            Card(suit, rank)
            for suit in self.new_deck_order_suits
            for rank in (
                ace_to_king
                if suit in (Suit.Spades, Suit.Diamonds)
                else king_to_ace
            )
        ]

    def shuffle(self, cards: list[Card]) -> list[Card]:
        if not cards:
            cards = self.cards

        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]

        return cards
