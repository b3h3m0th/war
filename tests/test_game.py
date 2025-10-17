from models.game import Game


def test_game_instantiation() -> None:
    game: Game = Game()

    assert game is not None
