from models.shell import Shell
from models.deck import Deck


def main():
    # shell: Shell = Shell()
    # shell.cmdloop()

    for card in Deck().cards:
        print(card)


if __name__ == "__main__":
    main()
