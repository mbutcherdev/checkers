# File contains all 'set' variables, such as the window size, the window title, etc.
# Change these values to change the game

# Import modules
import pygame

# --- Set up the pygame display window ---
WIDTH = 800
HEIGHT = 800
TITLE = "Checkers"
FPS = 60
# --- Set up the game board itself ---
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS
# --- Set up the colours ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKWOOD = (85, 52, 43)
WOOD = (210, 171, 111)  # Yellow-ish brown
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown_image.png'), (44, 25))
