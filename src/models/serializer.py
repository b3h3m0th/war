import json


class Serializer:
    def save(obj, path) -> None:
        with open(path, "w") as f:
            json.dump(obj.to_dict(), f, indent=4)

    def load(cls, path) -> None:
        with open(path, "r") as f:
            return cls.from_dict(json.load(f))
