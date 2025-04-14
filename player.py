import random
import copy

class Player:
    def __init__(self, symbol, max_depth=9):
        self.symbol = symbol
        self.opponent = 'O' if symbol == 'X' else 'X'
        self.max_depth = max_depth

    def min_max(self, state, is_maximizing, depth):
        winner = state.check_winner()
        if winner == self.symbol:
            return 10 - depth, None
        elif winner == self.opponent:
            return depth - 10, None
        elif state.no_winner() or depth >= self.max_depth:
            return 0, None
        
        best_score = float('-inf') if is_maximizing else float('inf')
        best_moves = []

        for move in state.empty_positions():
            new_state = copy.deepcopy(state)
            new_state.make_move(move, self.symbol if is_maximizing else self.opponent)
            score, _ = self.min_max(new_state, not is_maximizing, depth+1)

            if is_maximizing:
                if score > best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
            else:
                if score < best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
        
        chosen_move = random.choice(best_moves) if best_moves else None
        return best_score, chosen_move
    
    def choose_move(self, state):
        _, move = self.min_max(state, True, 0)
        return move

