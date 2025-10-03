from __future__ import annotations
import random

from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    cards: list[Card] = []

    def __init__(self, cards: list[Card] = []) -> None:
        self.cards = cards if cards else self.get_new_sorted_cards()

    def get_new_sorted_cards(self) -> list[Card]:
        new_deck_order_suits = [Suit.Spades, Suit.Diamonds, Suit.Clubs, Suit.Hearts]
        ace_to_king = [Rank.Ace, [rank for rank in Rank if rank is not Rank.Ace]]
        king_to_ace = [
            [rank[::-1] for rank in Rank if rank is not Rank.Ace],
            Rank.Ace,
        ]

        return [
            (
                Card(suit, rank)
                for rank in (
                    ace_to_king
                    if suit is Suit.Spades or ace_to_king is Suit.Diamonds
                    else king_to_ace
                )
            )
            for suit in new_deck_order_suits
        ]

    def shuffle(self, cards: list[Card]) -> list[Card]:
        if not cards:
            cards = self.cards

        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]

        return cards
