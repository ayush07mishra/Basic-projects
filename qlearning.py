import numpy as np
import random

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}  # state -> [Q values]
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0] * len(self.actions)
        return self.q_table[state]

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        q_vals = self.get_q_values(state)
        return int(np.argmax(q_vals))

    def update(self, state, action, reward, next_state):
        q_vals = self.get_q_values(state)
        next_q_vals = self.get_q_values(next_state)
        q_vals[action] = q_vals[action] + self.alpha * (reward + self.gamma * max(next_q_vals) - q_vals[action])
