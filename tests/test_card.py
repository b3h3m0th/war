from enums.rank import Rank
from enums.suit import Suit
from models.card import Card
from models.deck import Deck


def test_card_equality() -> None:
    card1 = Card(Suit.Spades, Rank.Ace)
    card2 = Card(Suit.Spades, Rank.Ace)
    assert card1 == card2

    card3 = Card(Suit.Clubs, Rank.Three)
    card4 = Card(Suit.Clubs, Rank.Three)
    assert card3 == card4

    card5 = Card(Suit.Hearts, Rank.Five)
    card5 != Deck()


def test_equal_card_hashes_are_equal() -> None:
    card1 = Card(Suit.Clubs, Rank.Five)
    card2 = Card(Suit.Clubs, Rank.Five)

    assert card1.__hash__() == card2.__hash__()


def test_picture_cards_have_correct_str() -> None:
    jack = Card(Suit.Clubs, Rank.Jack)
    queen = Card(Suit.Clubs, Rank.Queen)
    king = Card(Suit.Clubs, Rank.King)
    ace = Card(Suit.Clubs, Rank.Ace)

    assert jack.__str__() == "J♣"
    assert queen.__str__() == "Q♣"
    assert king.__str__() == "K♣"
    assert ace.__str__() == "A♣"


def test_card_suites_have_correct_str() -> None:
    spades = Card(Suit.Spades, Rank.Five)
    hearts = Card(Suit.Hearts, Rank.Five)
    clubs = Card(Suit.Clubs, Rank.Five)
    diamonds = Card(Suit.Diamonds, Rank.Five)

    assert spades.__str__() == "5♠"
    assert hearts.__str__() == "5♥"
    assert clubs.__str__() == "5♣"
    assert diamonds.__str__() == "5♦"
