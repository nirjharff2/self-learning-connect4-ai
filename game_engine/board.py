import numpy as np

class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.board = np.zeros((self.ROWS, self.COLS), dtype=int)

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[0][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.ROWS - 1, -1, -1):
            if self.board[r][col] == 0:
                return r
        return None

    def print_board(self):
        print(self.board, 0)

    def winning_move(self, piece):
        # horizontal
        for c in range(self.COLS - 3):
            for r in range(self.ROWS):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True
        # vertical
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True
        # diagonal /
        for c in range(self.COLS - 3):
            for r in range(self.ROWS - 3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True
        # diagonal \
        for c in range(self.COLS - 3):
            for r in range(3, self.ROWS):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True
        return False

    def reset(self):
        self.board.fill(0)

    def copy(self):
        b = Board()
        b.board = np.copy(self.board)
        return b
