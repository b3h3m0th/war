from models.shell import Shell
from models.deck import Deck


def main() -> None:
    shell: Shell = Shell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
