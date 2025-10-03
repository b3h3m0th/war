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
        return [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(numbers: list[int]) -> list[int]:
        for i in range(len(numbers) - 1, 0, -1):
            j = random.randint(0, i)
            numbers[i], numbers[j] = numbers[j], numbers[i]

        return numbers
