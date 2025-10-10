from __future__ import annotations
import random
from models.card import Card
from enums.suit import Suit
from enums.rank import Rank


class Deck:
    NEW_DECK_ORDER_SUITS = [
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
        king_to_ace = ace_to_king[::-1]

        return [
            Card(suit, rank)
            for suit in self.NEW_DECK_ORDER_SUITS
            for rank in (
                ace_to_king
                if suit in self.NEW_DECK_ORDER_SUITS[:2]
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

    def deal(self) -> Card:
        return self.cards.pop()

    def __eq__(self, other) -> bool:
        return isinstance(other, Deck) and self.cards == other.cards

    def __hash__(self) -> int:
        return hash(card for card in self.cards)

    def to_dict(self) -> dict:
        return {
            "cards": [card.to_dict() for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data: dict) -> Deck:
        return cls(Card.from_dict(card_data) for card_data in data["cards"])
