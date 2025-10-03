class Menu():



def print_menu():
    print()
    print("┌──────────────────────────────────┐")
    print("│               Menu               │")
    print("├──────────────────────────────────┤")
    print("│                                  │")
    print("│  (R)egister points               │")
    print("│  (S)how grades                   │")
    print("│  (E)xit                          │")
    print("│                                  │")
    print("├──────────[Danger zone]───────────┤")
    print("│                                  │")
    print("│  (Reset) points                  │")
    print("│                                  │")
    print("└──────────────────────────────────┘")


def main():
    register = {}

    while True:
        print_menu()
        option = input(">> ")
        if option == "R":
            name = input("\nEnter name: ")
            points = int(input("Enter points: "))
            if name in register:
                register[name] += points
            else:
                register[name] = points
        elif option == "S":
            display_grades(register)
        elif option == "Reset":
            register = {}
        elif option == "E":
            break


if __name__ == "__main__":
    main()
