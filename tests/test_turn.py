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


def test_initial_turns_are_equal() -> None:
    turn1 = Turn(Player("John", False), Card(Suit.Clubs, Rank.Two))
    turn2 = Turn(Player("John", False), Card(Suit.Clubs, Rank.Two))

    assert turn1 == turn2


def test_initial_round_hashes_are_equal() -> None:
    turn1 = Turn(Player("John", False), Card(Suit.Clubs, Rank.Two))
    turn2 = Turn(Player("John", False), Card(Suit.Clubs, Rank.Two))

    assert turn1.__hash__() == turn2.__hash__()


def test_different_rounds_not_equal():
    turn1 = Turn(Player("John", False), Card(Suit.Clubs, Rank.Two))
    turn2 = Turn(Player("Lisa", False), Card(Suit.Clubs, Rank.Three))

    assert turn1 != turn2
