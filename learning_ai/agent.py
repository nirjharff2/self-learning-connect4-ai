# learning_ai/agent.py

import random


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.95, epsilon=0.2):
        self.Q = {}   # normal dictionary (pickle-safe)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_values(self, state):
        """Ensure state exists in Q-table"""
        if state not in self.Q:
            self.Q[state] = [0] * 7
        return self.Q[state]

    def choose_action(self, state, valid_moves):
        """Epsilon-greedy action selection"""
        q_values = self.get_q_values(state)

        if random.random() < self.epsilon:
            return random.choice(valid_moves)

        return max(valid_moves, key=lambda c: q_values[c])

    def learn(self, state, action, reward, next_state, next_valid):
        """Q-learning update rule"""
        q_values = self.get_q_values(state)
        next_q = self.get_q_values(next_state)

        best_next = max((next_q[c] for c in next_valid), default=0)

        q_values[action] += self.alpha * (
            reward + self.gamma * best_next - q_values[action]
        )
