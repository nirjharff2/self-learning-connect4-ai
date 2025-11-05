# minimax_ai/test_ai.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_engine.board import Board
from minimax import minimax, pick_best_move_simple, AI_PIECE, PLAYER_PIECE
import random

def random_move(board):
    valid = [c for c in range(board.COLS) if board.is_valid_location(c)]
    return random.choice(valid) if valid else None

def play_game(ai_depth=3, verbose=False):
    board = Board()
    turn = 0
    while True:
        if turn == 0:
            col = random_move(board)
            if col is None:
                return 0  # draw
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, PLAYER_PIECE)
            if board.winning_move(PLAYER_PIECE):
                return -1  # player wins (random)
        else:
            col, score = minimax(board, ai_depth, -float('inf'), float('inf'), True)
            if col is None:
                col = pick_best_move_simple(board, AI_PIECE)
            if col is None:
                return 0  # draw
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, AI_PIECE)
            if board.winning_move(AI_PIECE):
                return 1  # AI wins
        turn ^= 1

if __name__ == "__main__":
    N = 20
    ai_wins = 0
    draws = 0
    losses = 0
    for i in range(N):
        res = play_game(ai_depth=3)
        if res == 1:
            ai_wins += 1
        elif res == -1:
            losses += 1
        else:
            draws += 1
    print(f"Out of {N} games: AI wins={ai_wins}, draws={draws}, losses={losses}")
