from unittest.mock import patch
from models.shell import Shell


def test_shell_instantiation() -> None:
    shell: Shell = Shell()

    assert shell is not None


def test_do_menu(capsys) -> None:
    shell: Shell = Shell()
    shell.do_menu("")
    captured = capsys.readouterr()
    output = captured.out
    expected_output = """\
┌──────────────────────────────────┐
│            WAR - Menu            │
├──────────────────────────────────┤
│                                  │
│  (rules) Shows game rules        │
│  (menu)  Shows the menu          │
│  (new)   Start new game          │
│  (log)   Game history            │
│  (help)  List commands           │
│  (quit)  Quit                    │
│                                  │
└──────────────────────────────────┘
"""

    assert expected_output.strip() in output


def test_starting_new_game_not_saving(
    tmp_path,
) -> None:  # tmp_path is a temporary empty director
    shell: Shell = Shell()
    shell.games_path = tmp_path  # Save game in temporary directory

    # Setting return values so tests will function
    with (
        patch("models.shell.choice", return_value=False),
        patch("models.game.choice", return_value=False),
        patch("builtins.input", return_value="test_save"),
    ):
        shell.do_new("")

    assert not any(
        tmp_path.iterdir()
    )  # Checks that the temporary directory is still empty
