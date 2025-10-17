from __future__ import annotations
from models.deck import Deck
from models.player import Player
from models.round import Round
from models.turn import Turn
from enums.variant import Variant

import datetime
from prompt_toolkit.shortcuts import choice


class Game:
    def __init__(
        self,
        players: list[Player] = None,
        variant: Variant = Variant.NoJoker,
        deck: Deck = None,
        rounds: list[Round] = None,
        name: str = None,
    ) -> None:
        self.variant = variant
        self.deck = deck or Deck()
        self.players = players or []
        self.rounds = rounds or []
        self.name = name or Game._get_timestamp_name()

    def start(self) -> None:
        """
        Starts the game
        """

        player_choice = choice(
            message="Choose a gamemode:",
            options=[
                ("pvc", "Player vs Computer"),
                ("pvp", "Player vs Player"),
            ],
            default="pvc",
        )

        if player_choice == "pvc":
            player = Player(input("Enter your name: ").strip())
            computer = Player("Computer", True)
            self.players = [player, computer]
        elif player_choice == "pvp":
            player1 = Player(input("Enter name for Player 1: ").strip())
            player2 = Player(input("Enter name for Player 2: ").strip())
            self.players = [player1, player2]

        self.deck.shuffle()

        round_counter: int = 0
        while len(self.deck.cards) >= len(self.players):
            round_counter += 1
            print(f"\nRound {round_counter}:")

            current_round = Round()
            self.rounds.append(current_round)

            for player in self.players:
                dealt_card = self.deck.deal()[0]
                current_turn = Turn(player, dealt_card)
                current_round.turns.append(current_turn)

                print(f"{player.name}: {dealt_card}")

            winning_turns = current_round.get_winning_turns()

            if len(winning_turns) > 1:
                tie_names = ", ".join(
                    f"{turn.player} ({turn.card})" for turn in winning_turns
                )
                print(f"Tie between: {tie_names}")
            elif len(winning_turns) == 1:
                winner = winning_turns[0]
                print(f"{winner.player} has the highest card ({winner.card})")

            # input("Press any key to continue to the next round")

        print()
        self.print_results()

    def print_results(self) -> None:
        wins_per_player: dict[Player, int] = {}
        ties: int = 0

        for played_round in self.rounds:
            turn_wins = played_round.get_winning_turns()
            if len(turn_wins) == 1:
                win = turn_wins[0]
                wins_per_player[win.player] = (
                    wins_per_player.get(win.player, 0) + 1
                )
            else:
                ties += 1

        print(f"Results for {self.name}:")
        for key, value in wins_per_player.items():
            print(f"{key} wins: {value}")

        print(f"Ties: {ties}")

    @classmethod
    def _get_timestamp_name(self, prefix: str = "game") -> str:
        """
        Returns a name for a Game based on the current time.
        Format: <prefix>_YYYY-MM-DD-hh-mm-ss-ms
        """

        return f"{prefix}_{(datetime.datetime
                            .now(datetime.timezone.utc)
                            .strftime("%Y-%m-%d-%H-%M-%S-%f"))}"

    def __eq__(self, other) -> bool:
        """
        Checks whether a Game is equal to another Game.
        Games are considered equal if their
        players, rounds, deck and variant are equal
        """

        return (
            isinstance(other, Game)
            and self.players == other
            and self.rounds == other.rounds
            and self.deck == other.deck
            and self.variant == other.variant
        )

    def __hash__(self) -> int:
        """
        Returns a hash based on the game its players, rounds, deck and variant
        """

        return hash(
            (tuple(self.players), tuple(self.rounds), self.deck, self.variant)
        )

    def to_dict(self) -> dict:
        """
        Converts a Game into a dictionary that can be stringified into json
        """

        return {
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds],
            "deck": self.deck.to_dict(),
            "variant": self.variant.to_dict(),
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Game:
        """
        Returns a Game based on a json dictionary
        """

        return cls(
            [Player.from_dict(p) for p in data["players"]],
            Variant.from_dict(data["variant"]),
            Deck.from_dict(data["deck"]),
            [Round.from_dict(r) for r in data["rounds"]],
            data["name"],
        )
