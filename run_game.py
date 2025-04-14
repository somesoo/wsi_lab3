from player import Player
from game import Game

if __name__ == "__main__":
    player_x = Player('X', max_depth=1)
    player_o = Player('O', max_depth=4)
    game = Game(player_x, player_o, visualize=True)
    game.play()