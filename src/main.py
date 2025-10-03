from models.shell import Shell
from models.deck import Deck


def main():
    # shell: Shell = Shell()
    # shell.cmdloop()

    deck: Deck = Deck()

    for card in deck.cards:
        print(f"{card.suit} {card.rank}")


if __name__ == "__main__":
    main()
