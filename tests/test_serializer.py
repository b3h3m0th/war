from utils.serializer import Serializer
from models.player import Player


class Dummy:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {"name": self.name, "value": self.value}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["value"])


def test_save_and_load_dummy(tmp_path):
    dummy = Dummy("test", 42)
    file_path = tmp_path / "data.json"

    Serializer.save(dummy, file_path)

    assert file_path.exists()

    loaded = Serializer.load(Dummy, file_path)

    assert isinstance(loaded, Dummy)
    assert loaded.name == "test"
    assert loaded.value == 42


def test_save_and_load_player(tmp_path):
    player = Player("John Doe", False)
    file_path = tmp_path / "data.json"

    Serializer.save(player, file_path)

    assert file_path.exists()

    loaded = Serializer.load(Player, file_path)

    assert isinstance(loaded, Player)
    assert loaded.name == "John Doe"
    assert loaded.isNPC == False
