import pygame
import time
from environment import Environment
from agent import Agent

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Autonomous Agent - Q Learning")

env = Environment()
agent = Agent()

episodes = 200

for ep in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    steps = 0

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        total_reward += reward
        steps += 1

        env.draw(screen)
        pygame.display.flip()
        time.sleep(0.05)

    print(f"Episode {ep+1}: Steps = {steps}, Reward = {total_reward}")

pygame.quit()
