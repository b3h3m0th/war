from models.shell import Shell


<<<<<<< Updated upstream
def main() -> None:
    shell: Shell = Shell()
    shell.cmdloop()
=======
def main():
    # shell: Shell = Shell()
    # shell.cmdloop()

    deck: Deck = Deck()

    for card in deck.cards:
        print(f"{card.suit} {card.rank}")
>>>>>>> Stashed changes


if __name__ == "__main__":
    main()
