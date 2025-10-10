from models.player import Player


def test_name() -> None:
    player = Player("John",False)
    assert player.name == "John"
    assert player.isNPC == False
