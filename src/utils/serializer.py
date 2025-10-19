from __future__ import annotations
import json
from pathlib import Path


class Serializer:
    @staticmethod
    def save(obj: object, path: Path) -> None:
        directory = path.parent
        directory.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as f:
            json.dump(obj.to_dict(), f, indent=2)

    @staticmethod
    def load(cls: Serializer, path: Path) -> object:
        with open(path, "r") as f:
            return cls.from_dict(json.load(f))
