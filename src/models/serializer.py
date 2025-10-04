import json


class Serializer:

    def save_to_file(obj, path):
        with open(path, "w") as f:
            json.dump(obj.to_dict(), f, indent=4)

def load_from_file(cls, path):
    with open(path, "r") as f:
        return cls.from_dict(json.load(f))   pass
