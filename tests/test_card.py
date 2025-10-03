from enums.rank import Rank
from enums.suit import Suit
from models.card import Card


def test_card_equality() -> None:
    card1 = Card(Suit.Spades, Rank.Ace)
    card2 = Card(Suit.Spades, Rank.Ace)
    assert card1 == card2

    card3 = Card(Suit.Clubs, Rank.Three)
    card4 = Card(Suit.Clubs, Rank.Three)
    assert card1 == card2
