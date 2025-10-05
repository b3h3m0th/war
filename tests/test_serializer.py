import json
from pathlib import Path
from utils.serializer import Serializer


class Dummy:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {"name": self.name, "value": self.value}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["value"])


def test_save_and_load(tmp_path):
    obj = Dummy("test", 42)
    file_path = tmp_path / "data.json"

    Serializer.save(obj, file_path)

    assert file_path.exists()
    with open(file_path) as f:
        data = json.load(f)
    assert data == {"name": "test", "value": 42}

    loaded = Serializer.load(Dummy, file_path)

    assert isinstance(loaded, Dummy)
    assert loaded.name == "test"
    assert loaded.value == 42
