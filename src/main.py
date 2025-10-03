from models.shell import Shell


def main():
    shell: Shell = Shell()
    shell.cmdloop()


if __name__ == "__main__":
    main()
