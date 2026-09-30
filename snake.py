from collections import deque
import random


class Snake:

    def __init__(self, free_cells):
        self.body = deque(self.spawn_snake_body(free_cells))

    def spawn_snake_body(self, free_cells):
        free = set(free_cells)
        bodies = []
        for i, j in free:
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                body = [(i + k * di, j + k * dj) for k in range(3)]
                if all(cord in free for cord in body):
                    bodies.append(body)
        return random.choice(bodies)

    def move(self, direction):
        
        head = self.body[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        self.body.appendleft(new_head)
        self.body.pop()
