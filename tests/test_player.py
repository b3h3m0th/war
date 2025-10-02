from models.player import Player


def test_name() -> None:
    player = Player("John")
    assert player.name == "John"
