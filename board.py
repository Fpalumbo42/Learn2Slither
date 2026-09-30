import random

class Board:

    def __init__(self):
        self.grid = []
        for i in range(10):
            if i == 0 or i == 9:
                row = ['W'] * 10
            else:
                row = ['W'] + ['0'] * 8 + ['W']
            self.grid.append(row)
        
        self.place_apple('R')
        self.place_apple('G')
        self.place_apple('G')
            
    def place_apple(self, color):
        # todo check if there is empty space to place apple
        empty_space_cord = []
 
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if row[j] == '0':
                    empty_space_cord.append((i, j))
        
        cord = random.choice(empty_space_cord)
        self.grid[cord[0]][cord[1]] = color

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.grid)
