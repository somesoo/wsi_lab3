from player import Player
from game import Game

def simulate_games(depth_x, depth_o, rounds=10):
    results = {"X": 0, "O": 0, "Draw": 0}
    for _ in range(rounds):
        player1 = Player('X', max_depth=depth_x)
        player2 = Player('O', max_depth=depth_o)
        game = Game(player1, player2, visualize=False)
        result = game.play()
        results[result] += 1

    return results

if __name__ == "__main__":
    print("Symulacja wszystkich kombinacji głębokości (1–9)\n")

    for depth_x in range(1, 10):
        for depth_o in range(1, 10):
            results = simulate_games(depth_x, depth_o, rounds=10)
            print(f"X(depth={depth_x}) vs O(depth={depth_o}) → {results}")
