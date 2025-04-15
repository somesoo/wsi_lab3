from state import State

def set_board(state, board_config):
    state.board = board_config

def test_row_win():
    state = State()
    set_board(state, [
        ['X', 'X', 'X'],
        [' ', 'O', ' '],
        ['O', ' ', 'O']
    ])
    assert state.check_winner() == 'X'

def test_col_win():
    state = State()
    set_board(state, [
        ['O', 'X', ' '],
        ['O', 'X', ' '],
        ['O', ' ', 'X']
    ])
    assert state.check_winner() == 'O'

def test_diag_win():
    state = State()
    set_board(state, [
        ['X', 'O', ' '],
        ['O', 'X', ' '],
        [' ', ' ', 'X']
    ])
    assert state.check_winner() == 'X'

def test_anti_diag_win():
    state = State()
    set_board(state, [
        [' ', 'O', 'O'],
        ['X', 'X', 'X'],
        ['O', 'O', ' ']
    ])
    assert state.check_winner() == 'X'

def test_no_win():
    state = State()
    set_board(state, [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ])
    assert state.check_winner() is None

if __name__ == "__main__":
    test_row_win()
    test_col_win()
    test_diag_win()
    test_anti_diag_win()
    test_no_win()
    print("✅ Wszystkie testy zaliczone!")
