from models.shell import Shell
from models.card import Card
from enums.rank import Rank
from enums.suit import Suit


def main() -> None:
    shell: Shell = Shell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
