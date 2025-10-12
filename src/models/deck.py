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
        """
        Instantiates a new Deck and sets its cards
        """

        self.cards: list[Card] = (
            cards if cards else self.get_new_deck_order_cards()
        )

    def get_new_deck_order_cards(self) -> list[Card]:
        """
        Returns a list of cards in typical new deck order NDO.
        Spades: Ace -> King
        Diamonds: Ace -> King
        Clubs: King -> Ace
        Hearts: King -> Ace
        """

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
        """
        Shuffles the cards of a deck based on the Fisher Yates algorithm
        """

        if not cards:
            cards = self.cards

        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]

        return cards

    def deal(self, amount: int = 1) -> list[Card]:
        """
        Returns the last card from the deck list
        or the first card assuming the cards are on a face down pile.
        """

        dealt: list[Card] = self.cards[-amount:]
        self.cards = self.cards[:-amount]

        return dealt

    def __eq__(self, other) -> bool:
        """
        Checks whether a Deck is equal to another Deck
        """

        return isinstance(other, Deck) and self.cards == other.cards

    def __hash__(self) -> int:
        """
        Computes a hash of a Deck based on its cards
        """

        return hash(card for card in self.cards)

    def to_dict(self) -> dict:
        """
        Converts a Deck into a dictionary that can be stringified into json
        """

        return {
            "cards": [card.to_dict() for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data: dict) -> Deck:
        """
        Creates and returns a Deck based on a json dictionary
        """

        return cls(Card.from_dict(card_data) for card_data in data["cards"])
