import pickle
from game_engine.board import Board

with open("learning_ai/q_table.pkl", "rb") as f:
    Q = pickle.load(f)

def board_to_state(board):
    return tuple(board.board.flatten())

def play():
    board = Board()
    turn = 1

    print("=== HUMAN vs LEARNING AI ===")
    board.print_board()

    while True:
        if turn == 1:
            col = int(input("Your move (0-6): "))
        else:
            state = board_to_state(board)
            valid = [c for c in range(board.COLS) if board.is_valid_location(c)]
            col = max(valid, key=lambda c: Q[state][c])
            print(f"AI plays {col}")

        if board.is_valid_location(col):
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, turn)
            board.print_board()

            if board.winning_move(turn):
                print("You win!" if turn == 1 else "AI wins!")
                break

            turn = 2 if turn == 1 else 1
