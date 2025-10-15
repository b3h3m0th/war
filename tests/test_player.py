from models.player import Player


def test_name() -> None:
    player = Player("John", False)

    assert player.name == "John"
    assert player.isNpc is False


def test_player_equality() -> None:
    player1 = Player("John", False)
    player2 = Player("John", False)
    player3 = Player("Lisa", False)
    player4 = Player("Lisa", True)

    assert player1 == player2
    assert player2 != player3
    assert player3 != player4
