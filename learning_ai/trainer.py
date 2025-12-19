# learning_ai/trainer.py

from game_engine.board import Board
from learning_ai.agent import QLearningAgent
import sqlite3
import pickle

PLAYER_1 = 1
PLAYER_2 = 2


def board_to_state(board):
    """Convert board to a hashable state"""
    return tuple(board.board.flatten())


def train(episodes=10000):
    agent = QLearningAgent()

    # statistics
    wins = 0
    losses = 0
    draws = 0

    # ---- DATABASE SETUP ----
    conn = sqlite3.connect("dashboard/db.sqlite")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        episode INTEGER,
        wins INTEGER,
        losses INTEGER,
        draws INTEGER
    )
    """)
    conn.commit()

    # ---- TRAINING LOOP ----
    for episode in range(1, episodes + 1):
        board = Board()
        turn = PLAYER_1
        history = []  # (state, action)

        while True:
            state = board_to_state(board)
            valid_moves = [c for c in range(board.COLS) if board.is_valid_location(c)]

            # DRAW
            if not valid_moves:
                draws += 1
                reward = 0
                break

            action = agent.choose_action(state, valid_moves)
            row = board.get_next_open_row(action)
            board.drop_piece(row, action, turn)

            history.append((state, action))

            # WIN CHECK
            if board.winning_move(turn):
                if turn == PLAYER_1:
                    wins += 1
                    reward = 1
                else:
                    losses += 1
                    reward = -1
                break

            # switch turn
            turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

        # ---- LEARNING STEP ----
        for s, a in history:
            agent.learn(s, a, reward, state, valid_moves)

        # ---- EPSILON DECAY ----
        agent.epsilon = max(0.01, agent.epsilon * 0.999)

        # ---- LOG TO DATABASE EVERY 500 EPISODES ----
        if episode % 500 == 0:
            cur.execute(
                "INSERT INTO stats VALUES (?,?,?,?)",
                (episode, wins, losses, draws)
            )
            conn.commit()
            print(f"Episode {episode} | W:{wins} L:{losses} D:{draws}")

    conn.close()

    # ---- SAVE TRAINED MODEL ----
    with open("learning_ai/q_table.pkl", "wb") as f:
        pickle.dump(agent.Q, f)

    print("Training finished!")
    print(f"Final stats -> Wins:{wins}, Losses:{losses}, Draws:{draws}")
