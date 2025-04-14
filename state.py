class State:
    def __init__(self):
        self.board = [[' '] *3 for _ in range(3)]
        # Create the game board
        # board = [[' ', ' ', ' '],
        #          [' ', ' ', ' '],
        #          [' ', ' ', ' ']]

    def print_board(self):
        print('-' * 5)
        for i in self.board:
            print('|'.join(i))
            print('-' * 5)

    def empty_positions(self):
        return [(i,j) for i in range(3) for j in range(3) if self.board[i][j]==' ']

    def make_move(self, move, player):
        x, y = move
        self.board[x][y] = player

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
    def no_winner(self):
        return all(cell != ' ' for row in self.board for cell in row)