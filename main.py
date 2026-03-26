from pack import open_pack
from file_handler import save_cards, load_cards

def main():

    while True:
        print("\n1. open pack")
        print("2. view collection")
        print("3. exit")

        choice = input("choose: ")

        if choice == "1":
            cards = open_pack()

            print("\nyou got: ")
            for card in cards:
                print(card.display())

            save_cards(cards)

        elif choice == "2":
            cards = load_cards()

            print("\nYour cards: ")
            for card in cards:
                print(card)

        elif choice == "3":
            break

        else:
            print("Invalid choice")