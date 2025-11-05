# minimax_ai/minimax.py

import math
import random
from copy import deepcopy

# Constants for pieces
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4

# We'll import Board at runtime in functions that need it to avoid import-time issues
# Use run from project root so game_engine is importable.

def score_window(window, piece):
    """Score a 4-cell window for the given piece."""
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score_position(board_obj, piece):
    """
    Evaluate board and return a numeric score favouring `piece`.
    board_obj is an instance of Board (from game_engine.board).
    """
    board = board_obj.board.tolist()  # nested lists
    rows = board_obj.ROWS
    cols = board_obj.COLS
    score = 0

    # Score center column
    center_col = [board[r][cols // 2] for r in range(rows)]
    center_count = center_col.count(piece)
    score += center_count * 3

    # Horizontal
    for r in range(rows):
        row_array = [board[r][c] for c in range(cols)]
        for c in range(cols - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += score_window(window, piece)

    # Vertical
    for c in range(cols):
        col_array = [board[r][c] for r in range(rows)]
        for r in range(rows - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += score_window(window, piece)

    # Positive sloped diagonals
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += score_window(window, piece)

    # Negative sloped diagonals
    for r in range(3, rows):
        for c in range(cols - 3):
            window = [board[r - i][c + i] for i in range(WINDOW_LENGTH)]
            score += score_window(window, piece)

    return score

def get_valid_locations(board_obj):
    """Return list of valid column indices."""
    valid_locations = []
    for col in range(board_obj.COLS):
        if board_obj.is_valid_location(col):
            valid_locations.append(col)
    return valid_locations

def is_terminal_node(board_obj):
    """Check terminal: win or board full"""
    return board_obj.winning_move(PLAYER_PIECE) or board_obj.winning_move(AI_PIECE) or len(get_valid_locations(board_obj)) == 0

def minimax(board_obj, depth, alpha, beta, maximizingPlayer):
    """
    Minimax with alpha-beta pruning.
    Returns (best_col, best_score)
    """
    import game_engine.board as gb  # runtime import to ensure module path works
    valid_locations = get_valid_locations(board_obj)
    is_terminal = is_terminal_node(board_obj)

    if depth == 0 or is_terminal:
        if is_terminal:
            if board_obj.winning_move(AI_PIECE):
                return (None, 10_000_000)
            elif board_obj.winning_move(PLAYER_PIECE):
                return (None, -10_000_000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board_obj, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            row = board_obj.get_next_open_row(col)
            if row is None:
                continue
            # simulate
            temp_board = board_obj.copy()
            temp_board.drop_piece(row, col, AI_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (best_col, value)
    else:
        value = math.inf
        best_col = random.choice(valid_locations) if valid_locations else None
        for col in valid_locations:
            row = board_obj.get_next_open_row(col)
            if row is None:
                continue
            temp_board = board_obj.copy()
            temp_board.drop_piece(row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return (best_col, value)

def pick_best_move_simple(board_obj, piece):
    """Simple greedy fallback (pick best-scoring column)"""
    valid_locations = get_valid_locations(board_obj)
    best_score = -math.inf
    best_col = random.choice(valid_locations) if valid_locations else None
    for col in valid_locations:
        row = board_obj.get_next_open_row(col)
        temp_board = board_obj.copy()
        temp_board.drop_piece(row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col
