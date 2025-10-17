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

            keep_going = choice(
                message="Do you want to keep playing?",
                options=[
                    (True, "Yes"),
                    (False, "No, Quit"),
                ],
                default=True,
            )
            if not keep_going:
                break

        print()
        self.print_results()

    def print_results(self):
        """
        Shows the result of the current game
        """
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

        print("Results:")
        for key, value in wins_per_player.items():
            print(f"{key} wins: {value}")

        print(f"Ties: {ties}")

        winning_score = 0
        for player, wins in wins_per_player.items():
            if wins > winning_score:
                winning_score = wins

        winning_player = []
        for player, wins in wins_per_player.items():
            if wins == winning_score:
                winning_player.append(player)

        if len(winning_player) > 1:
            equlas_emoji = "🟰" * 36
            print(equlas_emoji)
            players_str = ", ".join(str(player) for player in winning_player)
            print(
                f"It's a draw between: {players_str} with "
                f"{winning_score} wins each! 🟰"
            )
            print(equlas_emoji)
        elif winning_player:
            winner = winning_player[0]
            confetti = "🎊🎉" * 18
            print(confetti)
            centered_msg = (
                f"{winner} wins this game with a score of {winning_score}"
            ).center(len(confetti))
            print(f"🎊🎉🎊 {centered_msg} 🎊🎉🎊")
            print(confetti)
