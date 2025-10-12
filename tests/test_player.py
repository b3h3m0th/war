from models.player import Player


def test_name() -> None:
    player = Player("John", False)

    assert player.name == "John"
    assert player.isNPC is False


def test_player_equality() -> None:
    player1 = Player("John", False)
    player2 = Player("John", False)
    player3 = Player("Lisa", False)

    assert player1 == player2
    assert player2 != player3
