import random
import pygame as pg


class Grid:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[random.randint(0, 1) for x in range(width)] for y in range(height)]

    def get_neigbours(self, x: int, y: int):
        neigbours = 0
        for y_off in range(-1, 2):
            if not -1 < y + y_off < self.height: continue
            for x_off in range(-1, 2):
                if not -1 < x + x_off < self.width: continue
                neigbours += self.grid[y + y_off][x + x_off]
        return neigbours - self.grid[y][x]

    def get_state(self, x: int, y: int, neighbours: int):
        state = self.grid[y][x]
        if state == 0 and neighbours == 3:
            return 1
        if state == 1 and not 2 <= neighbours <= 3:
            return 0
        return state

    def update(self):
        self.grid = [[self.get_state(x, y, self.get_neigbours(x, y)) for x in range(self.height)] for y in
                     range(self.width)]

    def draw(self, window, cellsize: int):
        for y in range(self.height):
            for x in range(self.width):
                pg.draw.rect(window, (255, 255, 255) if self.grid[y][x] == 1 else (0, 0, 0),
                             pg.Rect((x * cellsize, y * cellsize, cellsize, cellsize)))