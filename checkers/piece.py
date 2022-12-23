import pygame

from .constants import SQUARE_SIZE, WHITE, CROWN


class Piece:
    """
    Represents a piece on the board
    """
    padding = 25
    outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):  # Calcs the position in the dead centre of the square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(window, WHITE, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def __repr__(self):
        return str(self.color)
