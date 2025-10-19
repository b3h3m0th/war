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
        self: Game,
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

    def start(self: Game, taken_player_names: list[str]) -> None:
        """
        Starts the game
        """

        player_choice = choice(
            message="Choose a gamemode:",
            options=[
                ("pvc", "Player vs Computer"),
                ("pvp", "Player vs Player"),
                ("pvcc", "Player vs Computer with instant result(cheat mode)"),
                ("pvpc", "Player vs Player with instant result(cheat mode)"),
            ],
            default="pvc",
        )

        if player_choice == "pvc" or player_choice == "pvcc":
            player = Player(Game._input_name(taken_player_names))
            computer = Player("Computer", True)
            self.players = [player, computer]
        elif player_choice == "pvp" or player_choice == "pvpc":
            player1 = Player(Game._input_name(taken_player_names))
            player2 = Player(
                Game._input_name(taken_player_names + [player1.name])
            )
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

                if len(self.deck.cards) >= 3 + len(self.players):
                    self.deck.deal(3)
                    print("⚔️ You are going to WAR (burned three cards)")
                else:
                    print("️⚔️ Not enough cards left to go to WAR")

            elif len(winning_turns) == 1:
                winner = winning_turns[0]
                print(f"{winner.player} has the highest card ({winner.card})")

            if player_choice == "pvc" or player_choice == "pvp":
                keep_going = choice(
                    message="Do you want to keep playing?",
                    options=[(True, "Yes"), (False, "No, Quit")],
                    default=True,
                )
                if not keep_going:
                    break

        print()
        self.print_results()

    def get_results(self: Game) -> dict[Player, int]:
        """
        Returns a dictionary of all players
        and their amount of won rounds
        """

        wins_per_player: dict[Player, int] = {}

        for round in self.rounds:
            winning_turns = round.get_winning_turns()
            if len(winning_turns) == 1:
                win = winning_turns[0]
                wins_per_player[win.player] = (
                    wins_per_player.get(win.player, 0) + 1
                )

        return wins_per_player

    def print_results(self: Game, results: dict[Player, int] = None) -> None:
        """
        Prints the result of the current game
        """

        results = results or self.get_results()
        max_score = max(results.values())
        winning_results = {k: v for k, v in results.items() if v == max_score}

        if len(winning_results) > 1:
            players_str = ", ".join(
                str(player) for player in winning_results.keys()
            )
            print(
                f"👔 It's a draw between: {players_str} with "
                f"{max_score} wins each."
            )
        else:
            winner_str = f"{list(winning_results.items())[0][0]} \
                won {self.name} with a score of {max_score}"
            print(f"🎉 {winner_str}")

        for player, wins in results.items():
            print(f"{player} wins: {wins}")

        print()

    @classmethod
    def _input_name(cls: Game, taken_names: list[str]) -> Player:
        while True:
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty")
            elif name in taken_names:
                print("Name already in use")
            else:
                return name

    @classmethod
    def _get_timestamp_name(cls: Game, prefix: str = "game") -> str:
        """
        Returns a name for a Game based on the current time.
        Format: <prefix>_YYYY-MM-DD-hh-mm-ss-ms
        """

        return f"{prefix}_{(datetime.datetime
                            .now(datetime.timezone.utc)
                            .strftime("%Y-%m-%d-%H-%M-%S-%f"))}"

    def __eq__(self: Game, other: Game) -> bool:
        """
        Checks whether a Game is equal to another Game.
        Games are considered equal if their
        players, rounds, deck and variant are equal.
        """

        return (
            isinstance(other, Game)
            and self.players == other
            and self.rounds == other.rounds
            and self.deck == other.deck
            and self.variant == other.variant
        )

    def __hash__(self: Game) -> int:
        """
        Returns a hash based on the game its players, rounds, deck and variant
        """

        return hash(
            (tuple(self.players), tuple(self.rounds), self.deck, self.variant)
        )

    def to_dict(self: Game) -> dict:
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
    def from_dict(cls: Game, data: dict) -> Game:
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
