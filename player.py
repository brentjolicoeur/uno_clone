

class Player:
    def __init__(self, name, cpu=True):
        self.name = name
        self.hand = []
        self.cpu = cpu

    def __repr__(self):
        return self.name