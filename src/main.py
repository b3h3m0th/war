from models.shell import Shell
from models.deck import Deck

from enums.rank import Rank
from enums.suit import Suit


def main():
    # shell: Shell = Shell()
    # shell.cmdloop()

    deck: Deck = Deck()

    for suit in Suit:
        for rank in Rank:
            print(f"{suit} {rank}")


if __name__ == "__main__":
    main()
