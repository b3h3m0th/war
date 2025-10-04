import json
from pathlib import Path


class Serializer:
    @staticmethod
    def save(obj: any, path: Path | str) -> None:
        with open(path, "w") as f:
            json.dump(obj.to_dict(), f, indent=4)

    @staticmethod
    def load(cls, path) -> None:
        with open(path, "r") as f:
            return cls.from_dict(json.load(f))
