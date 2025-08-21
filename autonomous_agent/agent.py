from qlearning import QLearningAgent

class Agent:
    def __init__(self):
        self.actions = [0, 1, 2, 3]  # 0: up, 1: down, 2: left, 3: right
        self.model = QLearningAgent(self.actions)

    def choose_action(self, state):
        return self.model.select_action(state)

    def learn(self, state, action, reward, next_state):
        self.model.update(state, action, reward, next_state)
