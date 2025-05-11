import pygame as pg
import time

""" This is pygame application, made on history lesson
    @name: GRAVITY SIMULATOR
    @author: Vadim
"""


# GLOBAL VARS
_WH = 600
_WH = 600
# TODO: g, metr to pixel

#colors
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball(object):
    def __init__(self, size:int, posx, posy):
        self.size = size
        self.posx = posx
        self.posy = posy

    def draw(self, window):
        pg.draw.circle(window, BLUE, self.posx, self.posy)

def fps_control():
    pass

def render(window):
    window.fill((100, 100, 100))
    for object in objects:
        object.draw(window)
    pg.display.flip()

def mainloop(window) -> int:
    running = 1
    stdsize = 0.5
    objects = []
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                b = Ball(stdsize, *event.pos)
                objects.append(b)

    render(window)
    
    return 0


def main():
    window = pg.display.set_mode((_WH, _WH))

    #DEBUG
    exit_mode = mainloop(window)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()