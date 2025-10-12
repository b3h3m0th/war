from models.turn import Turn
from models.player import Player
from models.card import Card

from enums.suit import Suit
from enums.rank import Rank


def test_turn_instantiation() -> None:
    player: Player = Player("John", False)
    card: Card = Card(Suit.Clubs, Rank.Five)

    turn: Turn = Turn(player, card)

    assert turn.player == player
    assert turn.card == card
