# Imports
import pygame as pg
import sys

# Init pygame
pg.init()

# Constants and variables
SCREEN_W = 800
SCREEN_H = 600
BG_COLOR = (0, 0, 0)
L_PADDLE_COLOR = (255, 0, 0)
R_PADDLE_COLOR = (255, 255, 0)

screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
pg.display.set_caption("Pong")
clock = pg.time.Clock()
running = True

l_paddle = pg.Rect(20, SCREEN_H // 2 - 60, 20, 120)
r_paddle = pg.Rect(SCREEN_W - 40, SCREEN_H // 2 - 60, 20, 120)

# Game loop
while running:
    # Make sure clicking X closes the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Set bg color
    screen.fill(BG_COLOR)

    # Draw stuff
    pg.draw.rect(screen, L_PADDLE_COLOR, l_paddle)
    pg.draw.rect(screen, R_PADDLE_COLOR, r_paddle)

    # Update the screen
    pg.display.flip()

    # Lock fps to 60
    clock.tick(60)

# Exit
pg.quit()
sys.exit()
