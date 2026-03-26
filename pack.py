import random
from card import card, RareCard

common = ["caitlin", "vi", "jinx", "echo", "jayce", "victor", "heimerdinger", "silco", "mel", "vander"]
rare = ["beast vander", "glorious evolution victor", "powder", "monkey bomb", "arcane empath mel"]

def get_card():
    """
    returns a random card
    """

    number = random.randint(1, 10)

    if number <= 7:
        return card(random.choice(common), "common")
    else:
        return RareCard(random.choice(rare))
    
def open_pack():
        """
        return 5 cards
        """
        cards = []

        for i in range(3):
            cards.append(get_card())
            return cards