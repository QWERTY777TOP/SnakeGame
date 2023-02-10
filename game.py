import pygame as pg
from field import Grid

class Game:

    def __init__(self, width: int, height : int, cellsize : int):
        pg.init()
        self.cellsize = cellsize
        self.window = pg.display.set_mode((width * cellsize, height * cellsize))
        self.grid = Grid(width, height)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
            self.grid.update()
            self.grid.draw(self.window, self.cellsize)
            pg.display.update()