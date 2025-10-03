from models.deck import Deck


def test_initial_deck_cards_count() -> None:
    deck = Deck()
    assert len(deck.cards) == 52


def test_initial_deck_cards_order() -> None:
    deck = Deck()
    for card in deck.cards:
        assert 
