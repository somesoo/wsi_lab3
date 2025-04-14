from state import State
import time

class Game:
    def __init__(self, player1, player2, visualize=True):
        self.state = State()
        self.players = [player1, player2]
        self.visualize = visualize

    def play(self):
        current = 0
        if self.visualize:
            print("Start")

        while True:
            player = self.players[current]
            move = player.choose_move(self.state)
            self.state.make_move(move, player.symbol)

            if self.visualize:
                print(f"{player.symbol} move: {move}")
                self.state.print_board()
                time.sleep(0.5)

            winner = self.state.check_winner()
            if winner:
                if self.visualize:
                    print(f"Winner: {winner}")
                return winner
            elif self.state.no_winner():
                if self.visualize:
                    print("Draw")
                return "Draw"
            
            current = 1 - current