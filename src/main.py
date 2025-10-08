from models.shell import Shell
from models.card import Card
from enums.rank import Rank
from enums.suit import Suit


def main() -> None:
    # shell: Shell = Shell()
    # shell.cmdloop()

    card1 = Card(Suit.Clubs, Rank.Ace)
    card2 = Card(Suit.Clubs, Rank.King)
    shell = Shell()

    print(card1.__eq__(shell))


if __name__ == "__main__":
    main()
