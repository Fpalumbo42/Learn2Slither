from board import Board
from snake import Snake


class Game:

    def __init__(self):
        self.board = Board()
        self.snake = Snake(self.board.empty_cells())
        for cord in self.snake.body:
            self.board.set_cell(cord, 'S')
        self.board.set_cell(self.snake.body[0], 'H')
        self.board.place_apple('G')
        self.board.place_apple('G')
        self.board.place_apple('R')
