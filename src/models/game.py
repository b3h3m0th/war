from models.deck import Deck
from models.player import Player
from models.round import Round
from models.turn import Turn
from enums.variant import Variant

from prompt_toolkit.shortcuts import choice


class Game:
    def __init__(
        self, players: list[Player] = None, variant: Variant = Variant.NoJoker
    ) -> None:
        self.variant = variant
        self.deck = Deck()
        self.players = players
        self.rounds = players or []

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
            print(f"\nRound {round_counter}" + "-" * 20)

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
                print(
                    f"{winner.player} has the highest card " f"({winner.card})"
                )

            # input("Press any key to continue to the next round")

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

        print("Result:")
        for key, value in wins_per_player.items():
            print(f"{key}: {value}")

        print(f"Ties: {ties}")
