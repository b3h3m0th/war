from models.deck import Deck
from enums.suit import Suit
from enums.rank import Rank
from models.card import Card
import random


def test_initial_deck_cards_count() -> None:
    deck = Deck()
    assert len(deck.cards) == 52


def test_initial_deck_cards_order() -> None:
    expected_deck_order = [
        Card(Suit.Spades, Rank.Ace),
        Card(Suit.Spades, Rank.Two),
        Card(Suit.Spades, Rank.Three),
        Card(Suit.Spades, Rank.Four),
        Card(Suit.Spades, Rank.Five),
        Card(Suit.Spades, Rank.Six),
        Card(Suit.Spades, Rank.Seven),
        Card(Suit.Spades, Rank.Eight),
        Card(Suit.Spades, Rank.Nine),
        Card(Suit.Spades, Rank.Ten),
        Card(Suit.Spades, Rank.Jack),
        Card(Suit.Spades, Rank.Queen),
        Card(Suit.Spades, Rank.King),
        Card(Suit.Diamonds, Rank.Ace),
        Card(Suit.Diamonds, Rank.Two),
        Card(Suit.Diamonds, Rank.Three),
        Card(Suit.Diamonds, Rank.Four),
        Card(Suit.Diamonds, Rank.Five),
        Card(Suit.Diamonds, Rank.Six),
        Card(Suit.Diamonds, Rank.Seven),
        Card(Suit.Diamonds, Rank.Eight),
        Card(Suit.Diamonds, Rank.Nine),
        Card(Suit.Diamonds, Rank.Ten),
        Card(Suit.Diamonds, Rank.Jack),
        Card(Suit.Diamonds, Rank.Queen),
        Card(Suit.Diamonds, Rank.King),
        Card(Suit.Clubs, Rank.King),
        Card(Suit.Clubs, Rank.Queen),
        Card(Suit.Clubs, Rank.Jack),
        Card(Suit.Clubs, Rank.Ten),
        Card(Suit.Clubs, Rank.Nine),
        Card(Suit.Clubs, Rank.Eight),
        Card(Suit.Clubs, Rank.Seven),
        Card(Suit.Clubs, Rank.Six),
        Card(Suit.Clubs, Rank.Five),
        Card(Suit.Clubs, Rank.Four),
        Card(Suit.Clubs, Rank.Three),
        Card(Suit.Clubs, Rank.Two),
        Card(Suit.Clubs, Rank.Ace),
        Card(Suit.Hearts, Rank.King),
        Card(Suit.Hearts, Rank.Queen),
        Card(Suit.Hearts, Rank.Jack),
        Card(Suit.Hearts, Rank.Ten),
        Card(Suit.Hearts, Rank.Nine),
        Card(Suit.Hearts, Rank.Eight),
        Card(Suit.Hearts, Rank.Seven),
        Card(Suit.Hearts, Rank.Six),
        Card(Suit.Hearts, Rank.Five),
        Card(Suit.Hearts, Rank.Four),
        Card(Suit.Hearts, Rank.Three),
        Card(Suit.Hearts, Rank.Two),
        Card(Suit.Hearts, Rank.Ace),
    ]

    deck = Deck()
    for expected, actual in zip(expected_deck_order, deck.cards):
        assert actual.suit == expected.suit
        assert actual.rank == expected.rank


def test_deck_equality() -> None:
    deck1 = Deck()
    deck2 = Deck()

    assert deck1.cards == deck2.cards

    deck3 = Deck()
    deck4 = Deck()

    deck3.cards = [
        Card(Suit.Spades, Rank.Ace),
        Card(Suit.Spades, Rank.Two),
        Card(Suit.Spades, Rank.Three),
        Card(Suit.Spades, Rank.Four),
        Card(Suit.Spades, Rank.Five),
        Card(Suit.Spades, Rank.Six),
        Card(Suit.Spades, Rank.Seven),
        Card(Suit.Spades, Rank.Eight),
        Card(Suit.Spades, Rank.Nine),
        Card(Suit.Spades, Rank.Ten),
        Card(Suit.Spades, Rank.Jack),
        Card(Suit.Spades, Rank.Queen),
        Card(Suit.Spades, Rank.King),
        Card(Suit.Diamonds, Rank.Ace),
        Card(Suit.Diamonds, Rank.Two),
        Card(Suit.Diamonds, Rank.Three),
        Card(Suit.Diamonds, Rank.Four),
        Card(Suit.Diamonds, Rank.Five),
        Card(Suit.Diamonds, Rank.Six),
        Card(Suit.Diamonds, Rank.Seven),
        Card(Suit.Diamonds, Rank.Eight),
        Card(Suit.Diamonds, Rank.Nine),
        Card(Suit.Diamonds, Rank.Ten),
        Card(Suit.Diamonds, Rank.Jack),
        Card(Suit.Diamonds, Rank.Queen),
        Card(Suit.Diamonds, Rank.King),
        Card(Suit.Clubs, Rank.King),
        Card(Suit.Clubs, Rank.Queen),
        Card(Suit.Clubs, Rank.Jack),
        Card(Suit.Clubs, Rank.Ten),
        Card(Suit.Clubs, Rank.Nine),
        Card(Suit.Clubs, Rank.Eight),
        Card(Suit.Clubs, Rank.Seven),
        Card(Suit.Clubs, Rank.Six),
        Card(Suit.Clubs, Rank.Five),
        Card(Suit.Clubs, Rank.Four),
        Card(Suit.Clubs, Rank.Three),
        Card(Suit.Clubs, Rank.Two),
        Card(Suit.Clubs, Rank.Ace),
        Card(Suit.Hearts, Rank.King),
        Card(Suit.Hearts, Rank.Queen),
        Card(Suit.Hearts, Rank.Jack),
        Card(Suit.Hearts, Rank.Ten),
        Card(Suit.Hearts, Rank.Nine),
        Card(Suit.Hearts, Rank.Eight),
        Card(Suit.Hearts, Rank.Seven),
        Card(Suit.Hearts, Rank.Six),
        Card(Suit.Hearts, Rank.Five),
        Card(Suit.Hearts, Rank.Four),
        Card(Suit.Hearts, Rank.Three),
        Card(Suit.Hearts, Rank.Two),
        Card(Suit.Hearts, Rank.Ace),
    ]

    deck4.cards = [
        Card(Suit.Spades, Rank.Ace),
        Card(Suit.Spades, Rank.Two),
        Card(Suit.Spades, Rank.Three),
        Card(Suit.Spades, Rank.Four),
        Card(Suit.Spades, Rank.Five),
        Card(Suit.Spades, Rank.Six),
        Card(Suit.Spades, Rank.Seven),
        Card(Suit.Spades, Rank.Eight),
        Card(Suit.Spades, Rank.Nine),
        Card(Suit.Spades, Rank.Ten),
        Card(Suit.Spades, Rank.Jack),
        Card(Suit.Spades, Rank.Queen),
        Card(Suit.Spades, Rank.King),
        Card(Suit.Diamonds, Rank.Ace),
        Card(Suit.Diamonds, Rank.Two),
        Card(Suit.Diamonds, Rank.Three),
        Card(Suit.Diamonds, Rank.Four),
        Card(Suit.Diamonds, Rank.Five),
        Card(Suit.Diamonds, Rank.Six),
        Card(Suit.Diamonds, Rank.Seven),
        Card(Suit.Diamonds, Rank.Eight),
        Card(Suit.Diamonds, Rank.Nine),
        Card(Suit.Diamonds, Rank.Ten),
        Card(Suit.Diamonds, Rank.Jack),
        Card(Suit.Diamonds, Rank.Queen),
        Card(Suit.Diamonds, Rank.King),
        Card(Suit.Clubs, Rank.King),
        Card(Suit.Clubs, Rank.Queen),
        Card(Suit.Clubs, Rank.Jack),
        Card(Suit.Clubs, Rank.Ten),
        Card(Suit.Clubs, Rank.Nine),
        Card(Suit.Clubs, Rank.Eight),
        Card(Suit.Clubs, Rank.Seven),
        Card(Suit.Clubs, Rank.Six),
        Card(Suit.Clubs, Rank.Five),
        Card(Suit.Clubs, Rank.Four),
        Card(Suit.Clubs, Rank.Three),
        Card(Suit.Clubs, Rank.Two),
        Card(Suit.Clubs, Rank.Ace),
        Card(Suit.Hearts, Rank.King),
        Card(Suit.Hearts, Rank.Queen),
        Card(Suit.Hearts, Rank.Jack),
        Card(Suit.Hearts, Rank.Ten),
        Card(Suit.Hearts, Rank.Nine),
        Card(Suit.Hearts, Rank.Eight),
        Card(Suit.Hearts, Rank.Seven),
        Card(Suit.Hearts, Rank.Six),
        Card(Suit.Hearts, Rank.Five),
        Card(Suit.Hearts, Rank.Four),
        Card(Suit.Hearts, Rank.Three),
        Card(Suit.Hearts, Rank.Two),
        Card(Suit.Hearts, Rank.Ace),
    ]

    assert deck3.cards == deck4.cards


def test_deal() -> None:
    deck = Deck()
    assert len(deck.cards) == 52

    dealt = deck.deal()

    assert len(deck.cards) == 51
    assert dealt == Card(Suit.Hearts, Rank.Ace)


def test_shuffle():
    deck = Deck()
    cards_before = deck.cards.copy()

    random.seed(42)
    shuffled = deck.shuffle(deck.cards.copy())

    # deterministic shuffle with seed
    random.seed(42)
    expected = Deck().shuffle(cards_before.copy())

    assert shuffled == expected
    assert shuffled != cards_before
