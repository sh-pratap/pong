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
R_PADDLE_COLOR = (147, 202, 237)
BALL_COLOR = (255, 255, 255)

screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
pg.display.set_caption("Pong")
clock = pg.time.Clock()
running = True

l_paddle = pg.Rect(20, SCREEN_H // 2 - 60, 20, 120)
r_paddle = pg.Rect(SCREEN_W - 40, SCREEN_H // 2 - 60, 20, 120)

ball_cords = (SCREEN_W // 2, SCREEN_H // 2)
ball_size = 15

# Game loop
while running:
    # Make sure clicking X closes the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # Get the keys pressed
    keys = pg.key.get_pressed()

    # Left paddle input
    if keys[pg.K_w] and l_paddle.y >= 0:
        l_paddle.y -= 5
    if keys[pg.K_s] and l_paddle.y + l_paddle.height <= SCREEN_H:
        l_paddle.y += 5

    # Right paddle input
    if keys[pg.K_UP] and r_paddle.y >= 0:
        r_paddle.y -= 5
    if keys[pg.K_DOWN] and r_paddle.y + r_paddle.height <= SCREEN_H:
        r_paddle.y += 5

    # Set bg color
    screen.fill(BG_COLOR)

    # Draw stuff
    pg.draw.rect(screen, L_PADDLE_COLOR, l_paddle)
    pg.draw.rect(screen, (255, 255, 255), l_paddle, 3)
    pg.draw.rect(screen, R_PADDLE_COLOR, r_paddle)
    pg.draw.rect(screen, (255, 255, 255), r_paddle, 3)
    pg.draw.circle(screen, BALL_COLOR, ball_cords, ball_size)
    pg.draw.line(screen, (255, 255, 255), (SCREEN_W // 2, 0),
                 (SCREEN_W // 2, SCREEN_H), 1)

    # Update the screen
    pg.display.flip()

    # Lock fps to 60
    clock.tick(60)

# Exit
pg.quit()
sys.exit()
