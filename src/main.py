from models.shell import Shell


def main() -> None:
    shell: Shell = Shell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
