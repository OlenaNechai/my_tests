class ElixirData:
    def __init__(self, **kwargs):
        self.name = "Amortentia" if "name" not in kwargs.keys() else kwargs['name']
        self.effect = "Love potion that causes a powerful infatuation or obsession in the drinker" \
            if "effect" not in kwargs.keys() else kwargs['effect']
        self.characteristics = "Mother-of-pearl sheen; Spiralling steam; " \
                               "Scent is multi-faceted and varies based on what the person likes" \
            if "characteristics" not in kwargs.keys() else kwargs['characteristics']
        self.difficulty = "Advanced" if "difficulty" not in kwargs.keys() else kwargs['difficulty']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
