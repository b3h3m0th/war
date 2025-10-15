from models.round import Round
from models.turn import Turn


def test_equal_values() -> None:
    round_1 = Round([Turn("Bob", 1), Turn("Bill", 1)])
    round_2 = Round([Turn("Bob", 1), Turn("Bill", 1)])
    assert round_1 == round_2


def test_empty_list() -> None:
    round = Round([])
    assert round.get_winning_turn() is None


def test_equal_cards() -> None:
    round = Round([Turn("Bob", 1), Turn("Bill", 1)])
    assert round.get_winning_turn() is None


def test_winner_first() -> None:
    round = Round([Turn("Bob", 2), Turn("Bill", 1)])
    assert round.get_winning_turn() == round.turns[0]


def test_winner_second() -> None:
    round = Round([Turn("Bob", 1), Turn("Bill", 2)])
    assert round.get_winning_turn() == round.turns[1]


def test_winner_third() -> None:
    round = Round(
        [Turn("Bob", 1), Turn("Bill", 1), Turn("Bob", 2), Turn("Bill", 1)]
    )
    assert round.get_winning_turn() == round.turns[2]


def test_winner_fourth() -> None:
    round = Round(
        [Turn("Bob", 1), Turn("Bill", 1), Turn("Bob", 1), Turn("Bill", 2)]
    )
    assert round.get_winning_turn() == round.turns[3]


def test_4_equal_cards() -> None:
    round = Round(
        [Turn("Bob", 1), Turn("Bill", 1), Turn("Bob", 1), Turn("Bill", 1)]
    )
    assert round.get_winning_turn() is None
