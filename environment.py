import pygame
import numpy as np

GRID_SIZE = 10
WINDOW_SIZE = 500
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

class Environment:
    def __init__(self):
        self.grid_size = GRID_SIZE
        self.start = (0, 0)
        self.goal = (9, 9)
        self.obstacles = {(3, 3), (3, 4), (4, 3), (6, 6), (7, 6), (8, 6)}
        self.reset()

    def reset(self):
        self.agent_pos = list(self.start)
        return tuple(self.agent_pos)

    def get_state(self):
        return tuple(self.agent_pos)

    def is_done(self):
        return tuple(self.agent_pos) == self.goal

    def step(self, action):
        x, y = self.agent_pos
        if action == 0: x -= 1
        elif action == 1: x += 1
        elif action == 2: y -= 1
        elif action == 3: y += 1

        if (0 <= x < self.grid_size) and (0 <= y < self.grid_size):
            if (x, y) not in self.obstacles:
                self.agent_pos = [x, y]

        reward = 100 if self.is_done() else -1
        return self.get_state(), reward, self.is_done()

    def draw(self, screen):
        screen.fill(WHITE)
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

        for ox, oy in self.obstacles:
            pygame.draw.rect(screen, BLACK, (ox*CELL_SIZE, oy*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, GREEN, (self.goal[0]*CELL_SIZE, self.goal[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, BLUE, (self.agent_pos[0]*CELL_SIZE + CELL_SIZE//2, self.agent_pos[1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//3)
