import json
from unittest.mock import patch
from models.game import Game
from models.shell import Shell


def test_shell_instantiation() -> None:
    shell: Shell = Shell()

    assert shell is not None


def test_shell_instantiation_prints_menu(capsys):
    Shell()
    captured = capsys.readouterr()
    assert "WAR - Menu" in captured.out


def test_do_rules_prints_rules(capsys):
    shell = Shell()
    shell.do_rules("")
    captured = capsys.readouterr()

    assert "Welcome to our version of Casino War!" in captured.out


def test_do_menu_prints_menu(capsys):
    shell = Shell()
    shell.do_menu("")
    captured = capsys.readouterr()

    assert "WAR - Menu" in captured.out


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
│  (chng)  Change player name      │
│  (help)  List commands           │
│  (quit)  Quit                    │
│                                  │
└──────────────────────────────────┘
"""

    assert expected_output.strip() in output


def test_do_quit_returns_true_and_prints(capsys):
    shell = Shell()
    result = shell.do_quit("")
    captured = capsys.readouterr()

    assert "Thank you for playing war" in captured.out
    assert result is True


def test_default_prints_unknown(capsys):
    shell = Shell()
    shell.default("foobar")
    captured = capsys.readouterr()
    assert 'Unknown option: "foobar"' in captured.out


def test_do_new_creates_game_and_does_not_save(tmp_path):
    shell = Shell()
    shell.games_path = tmp_path

    with (
        patch("models.shell.choice", return_value=False),
        patch("models.game.choice", side_effect=["pvc", False]),
        patch("builtins.input", return_value="Player1"),
    ):
        shell.do_new("")

    assert isinstance(shell.game, Game)
    assert shell.game.players
    assert not any(tmp_path.iterdir())


def test_do_rules(capsys) -> None:
    shell: Shell = Shell()
    shell.do_rules("")
    output = capsys.readouterr().out
    start = output.find("Welcome to our version of Casino War!")
    output = output[start:]
    assert "Welcome to our version of Casino War!" in output
    assert "At the start, you choose which game variant you" in output
    assert "In the basic War game, each player is dealt a card" in output
    assert "After each round, you will be asked if you want to draw" in output
    assert "Once you exit the current game, you will return to the" in output


def test_quit_game() -> None:
    shell: Shell = Shell()
    assert shell.do_quit("") is True


def test_get_previous_games(tmp_path) -> None:
    game_data = {
        "players": [
            {"name": "Bill", "isNpc": False},
            {"name": "Bob", "isNpc": False},
        ],
        "variant": {"value": "NoJoker"},
        "deck": {"cards": []},
        "rounds": [{"turns": []}],
        "name": "Test Game",
    }
    for i in range(2):
        (tmp_path / f"game_{i}.json").write_text(json.dumps(game_data))

    shell = Shell()
    shell.games_path = tmp_path  # point to temp dir

    games = shell.get_previous_games()

    assert isinstance(games, list)
    assert all(isinstance(g, Game) for g in games)
    assert len(games) == 2


def test_do_log_calls_print_results(tmp_path):
    game = Game()

    with patch.object(Shell, "get_previous_games", return_value=[game]):
        with patch.object(Game, "print_results") as mock_print:
            shell = Shell()
            shell.games_path = tmp_path
            shell.do_log("")
            mock_print.assert_called_once()
