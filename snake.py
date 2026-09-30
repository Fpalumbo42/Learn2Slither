from collections import deque

class snake():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snake_length = 3
        self.body = deque()
    
        