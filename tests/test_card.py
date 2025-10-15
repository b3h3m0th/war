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

    assert hash(card1) == hash(card2)


def test_picture_cards_have_correct_str() -> None:
    jack = Card(Suit.Clubs, Rank.Jack)
    queen = Card(Suit.Clubs, Rank.Queen)
    king = Card(Suit.Clubs, Rank.King)
    ace = Card(Suit.Clubs, Rank.Ace)

    assert str(jack) == "J♣"
    assert str(queen) == "Q♣"
    assert str(king) == "K♣"
    assert str(ace) == "A♣"


def test_card_suites_have_correct_str() -> None:
    spades = Card(Suit.Spades, Rank.Five)
    hearts = Card(Suit.Hearts, Rank.Five)
    clubs = Card(Suit.Clubs, Rank.Five)
    diamonds = Card(Suit.Diamonds, Rank.Five)

    assert str(spades) == "5♠"
    assert str(hearts) == "5♥"
    assert str(clubs) == "5♣"
    assert str(diamonds) == "5♦"
