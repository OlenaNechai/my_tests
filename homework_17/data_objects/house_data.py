class HouseData:
    def __init__(self, name, founder, animal, element, ghost):
        self.name = name
        self.founder = founder
        self.animal = animal
        self.element = element
        self.ghost = ghost

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs.get('name'), kwargs.get('founder'), kwargs.get('animal'), kwargs.get('element'),
                   kwargs.get('ghost'))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
