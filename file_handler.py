import csv

def save_cards(cards):
    """
    save cards to csv file
    """

    file = open("collection.csv", "a", newline="")
    writer = csv.writer(file)

    for Card in cards:
        writer.writerow([Card.name, Card.rarity])

    file.close()

def load_cards():
    """
    load cards from csv
    """
    cards = []
    try:
        file = open("collection.csv", "r")
        reader = csv.reader(file)

        for row in reader:
            cards.append(row)

        file.close()

    except:
        pass

    return cards