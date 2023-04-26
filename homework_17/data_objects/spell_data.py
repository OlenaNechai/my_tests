class SpellData:
    def __init__(self, **kwargs):
        self.name = "Unlocking Charm" if "name" not in kwargs.keys() else kwargs['name']
        self.incantation = "Alohomora" if "incantation" not in kwargs.keys() else kwargs['incantation']
        self.effect = "Unlocks objects" if "effect" not in kwargs.keys() else kwargs['effect']
        self.light = "Transparent" if "light" not in kwargs.keys() else kwargs['light']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
