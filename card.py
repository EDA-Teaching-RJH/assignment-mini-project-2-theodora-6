# card.py

class card:
    """
    basic card class for sorting name and rarity
    """

    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

        def display(self):
            return self.name + " - " + self.rarity

class RareCard(card):
    def __init__(self, name):
        super().__init__(name, "rare")
