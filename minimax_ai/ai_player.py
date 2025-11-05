# minimax_ai/ai_player.py
import sys, os
# Ensure project root (parent) is on sys.path so we can import game_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_engine.board import Board
from minimax import minimax, pick_best_move_simple, AI_PIECE, PLAYER_PIECE

def play_against_ai(depth=4):
    board = Board()
    game_over = False
    turn = 0  # 0 -> Player, 1 -> AI

    print("=== CONNECT 4: Human (1) vs AI (2) ===")
    board.print_board()

    while not game_over:
        if turn == 0:
            # Human turn
            try:
                col = int(input(f"Player (1), choose a column (0-{board.COLS-1}): "))
            except ValueError:
                print("Invalid input. Enter a number.")
                continue

            if col < 0 or col >= board.COLS:
                print("Column out of range.")
                continue

            if board.is_valid_location(col):
                row = board.get_next_open_row(col)
                board.drop_piece(row, col, PLAYER_PIECE)
                board.print_board()

                if board.winning_move(PLAYER_PIECE):
                    print("🎉 You win! 🎉")
                    game_over = True
            else:
                print("Column full. Try another.")
        else:
            # AI turn
            print("AI is thinking...")
            col, score = minimax(board, depth, -float('inf'), float('inf'), True)
            if col is None:
                # fallback
                col = pick_best_move_simple(board, AI_PIECE)
            if col is None:
                print("No valid moves left. It's a draw.")
                game_over = True
            else:
                row = board.get_next_open_row(col)
                board.drop_piece(row, col, AI_PIECE)
                print(f"AI plays column {col}")
                board.print_board()

                if board.winning_move(AI_PIECE):
                    print("💻 AI wins!")
                    game_over = True

        # Switch turn
        turn ^= 1

        # Check for draw
        if len([c for c in range(board.COLS) if board.is_valid_location(c)]) == 0 and not game_over:
            print("It's a draw!")
            game_over = True

if __name__ == "__main__":
    # default depth 4, change by running "python ai_player.py" optionally edit depth var
    play_against_ai(depth=4)
