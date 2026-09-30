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

    def empty_cells(self):
        empty_space_cord = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == '0':
                    empty_space_cord.append((i, j))
        return empty_space_cord

    def set_cell(self, cord, value):
        self.grid[cord[0]][cord[1]] = value

    def place_apple(self, color):
        # todo check if there is empty space to place apple
        self.set_cell(random.choice(self.empty_cells()), color)

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.grid)
