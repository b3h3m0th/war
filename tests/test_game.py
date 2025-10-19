from models.game import Game
from models.player import Player
from models.deck import Deck
from models.round import Round
from models.turn import Turn
from models.card import Card

from enums.variant import Variant
from enums.rank import Rank
from enums.suit import Suit

player1: Player = Player("John", False)
player2: Player = Player("John", False)
player3: Player = Player("Computer", True)

game1: Game = Game(
    [player1, player2],
    Variant.NO_JOKERS,
    Deck(),
    [
        Round(
            [
                Turn(player1, Card(Suit.Clubs, Rank.Ace)),
                Turn(player2, Card(Suit.Diamonds, Rank.Two)),
            ]
        ),
        Round(
            [
                Turn(player1, Card(Suit.Spades, Rank.Three)),
                Turn(player2, Card(Suit.Hearts, Rank.Eight)),
            ]
        ),
        Round(
            [
                Turn(player1, Card(Suit.Hearts, Rank.Ten)),
                Turn(player2, Card(Suit.Spades, Rank.Queen)),
            ]
        ),
    ],
    "test_game_1",
)
game2: Game = Game(
    [player1, player2],
    Variant.NO_JOKERS,
    Deck(),
    [
        Round(
            [
                Turn(player1, Card(Suit.Clubs, Rank.Ace)),
                Turn(player2, Card(Suit.Diamonds, Rank.Two)),
            ]
        ),
        Round(
            [
                Turn(player1, Card(Suit.Spades, Rank.Three)),
                Turn(player2, Card(Suit.Hearts, Rank.Eight)),
            ]
        ),
        Round(
            [
                Turn(player1, Card(Suit.Hearts, Rank.Ten)),
                Turn(player2, Card(Suit.Spades, Rank.Queen)),
            ]
        ),
    ],
    "test_game_1",
)
game3: Game = Game(
    [player2, player3],
    Variant.NO_JOKERS,
    Deck(),
    [
        Round(
            [
                Turn(player2, Card(Suit.Clubs, Rank.Ace)),
                Turn(player3, Card(Suit.Diamonds, Rank.Two)),
            ]
        ),
        Round(
            [
                Turn(player2, Card(Suit.Spades, Rank.Three)),
                Turn(player3, Card(Suit.Hearts, Rank.Eight)),
            ]
        ),
        Round(
            [
                Turn(player2, Card(Suit.Hearts, Rank.Ten)),
                Turn(player3, Card(Suit.Spades, Rank.Queen)),
            ]
        ),
    ],
    "test_game_2",
)


def test_game_instantiation() -> None:
    game: Game = Game()

    assert game is not None


def test_initial_rounds_empty() -> None:
    game: Game = Game()

    assert len(game.rounds) == 0


def test_games_equality() -> None:
    assert game1 == game2
    assert game2 != game3


def test_games_hashes() -> None:
    assert hash(game1) == hash(game2)
    assert hash(game2) != hash(game3)


def test_games_serialization() -> None:
    assert game1.to_dict() == game1.to_dict()
    assert game2.to_dict() != game3.to_dict()


def test_games_deserialization() -> None:
    assert Game.from_dict(game1.to_dict()) == Game.from_dict(game1.to_dict())
    assert Game.from_dict(game2.to_dict()) != Game.from_dict(game3.to_dict())
