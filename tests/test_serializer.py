from __future__ import annotations
from utils.serializer import Serializer
from models.player import Player


class Dummy:
    def __init__(self: Dummy, name: str, value: int) -> None:
        self.name = name
        self.value = value

    def to_dict(self: Dummy) -> dict:
        return {"name": self.name, "value": self.value}

    @classmethod
    def from_dict(cls: Dummy, data: dict) -> Dummy:
        return cls(data["name"], data["value"])


def test_save_and_load_dummy(tmp_path: str) -> None:
    dummy = Dummy("test", 42)
    file_path = tmp_path / "data.json"

    Serializer.save(dummy, file_path)

    assert file_path.exists()

    loaded = Serializer.load(Dummy, file_path)

    assert isinstance(loaded, Dummy)
    assert loaded.name == "test"
    assert loaded.value == 42


def test_save_and_load_player(tmp_path: str) -> None:
    player = Player("John Doe", False)
    file_path = tmp_path / "data.json"

    Serializer.save(player, file_path)

    assert file_path.exists()

    loaded = Serializer.load(Player, file_path)

    assert isinstance(loaded, Player)
    assert loaded.name == "John Doe"
    assert loaded.isNpc is False
