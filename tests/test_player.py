from models.player import Player


def test_name():
    player = Player("John")
    assert player.name == "John"
