from models.round import Round
from models.turn import Turn
from models.player import Player
from models.card import Card

from enums.suit import Suit
from enums.rank import Rank


def test_get_winning_turns_returns_single_turn() -> None:
    player1: Player = Player("John", False)
    player2: Player = Player("Lisa", False)

    card1: Card = Card(Suit.Clubs, Rank.Five)
    card2: Card = Card(Suit.Hearts, Rank.Ten)

    round: Round = Round([Turn(player1, card1), Turn(player2, card2)])
    turns: list[Turn] = round.get_winning_turns()

    assert len(turns) == 1
    assert turns[0].player == player2
    assert turns[0].card == card2


def test_get_winning_turns_returns_tie_correctly() -> None:
    player1: Player = Player("John", False)
    player2: Player = Player("Lisa", False)
    player3: Player = Player("Michael", False)

    card1: Card = Card(Suit.Clubs, Rank.King)
    card2: Card = Card(Suit.Hearts, Rank.King)
    card3: Card = Card(Suit.Spades, Rank.Eight)

    round: Round = Round(
        [Turn(player1, card1), Turn(player2, card2), Turn(player3, card3)]
    )
    turns: list[Turn] = round.get_winning_turns()

    assert len(turns) == 2
    assert turns[0].player == player1
    assert turns[0].card == card1
    assert turns[1].player == player2
    assert turns[1].card == card2


def test_get_winning_turns_returns_no_turns_correctly() -> None:
    round: Round = Round()
    turns: list[Turn] = round.get_winning_turns()

    assert len(turns) == 0
