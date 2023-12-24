import pygame as pg
from colors import Colors

class Grid: 
    def __init__(self): 
        self.num_rows = 20 
        self.num_cols = 10 
        self.cellSz = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_colors()

    def print_grid(self): 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                print(self.grid[i][j], end = " ")
            print()

    def is_inside(self, row, column):
        if 0 <= row < self.num_rows and 0 <= column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column): 
        if self.grid[row][column] == 0:
            return True
        return False
    
    def draw(self, screen): 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                cell_val = self.grid[i][j]
                cell_rect = pg.Rect(j *self.cellSz + 1, i * self.cellSz + 1, self.cellSz - 1, self.cellSz - 1)
                pg.draw.rect(screen,self.colors[cell_val],cell_rect)



    