from models.shell import Shell


def test_shell_instantiation() -> None:
    shell: Shell = Shell()

    assert shell != None
