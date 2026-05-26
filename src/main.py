import pygame as pg
import sys

pg.init()

SCREEN_W = 800
SCREEN_H = 600
BG_COLOR = (0, 0, 0)

screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
pg.display.set_caption("Pong")
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BG_COLOR)

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()
