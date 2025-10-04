class Player:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self):
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data):
        # Deserialize nested object
        address = Address.from_dict(data["address"])
        return cls(data["name"], data["age"], address)
