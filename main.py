# Checkers game written in Python and PyGame
# Developed in Python 3.11 using PyGame 2.1.3.dev8
import pygame
from checkers.constants import WIDTH, HEIGHT, TITLE, FPS, SQUARE_SIZE
from checkers.game import Game
from datetime import datetime

# Window setup
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)


def get_pos_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def get_time():
    time = datetime.now().strftime("%H:%M:%S")
    return time


def game_start_log(time):
    with open("log.txt", "w") as file:
        file.write(f"-- Checkers game log --\n"
                   f"Checkers game written in Python and PyGame by mbutcher.dev\n"
                   f"Developed in Python 3.11 using PyGame 2.1.3.dev8\n"
                   f"Game started at: {time}\n"
                   f"---\n")


def game_end_log(time):
    time_exit = get_time()
    t_total = datetime.strptime(time_exit, "%H:%M:%S") - datetime.strptime(time, "%H:%M:%S")
    with open("log.txt", "a") as file:
        file.write(f"---\n"
                   f"Game exit called: {time_exit}\n"
                   f"Time elapsed: {t_total}\n"
                   f"Programme closed.\n"
                   f"-- End of log --")


# Game loop
def main():
    time = get_time()
    game_start_log(time)
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Player exits game
                game_end_log(time)
                print("Thank you for playing!")
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()  # Exit pygame


main()
