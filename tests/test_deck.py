from models.deck import Deck


def test_initial_deck_order() -> None:
    deck = Deck()
    assert len(deck.cards) == 52
