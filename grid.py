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
    
    def is_full(self, row): 
        for i in range(self.num_cols): 
            if self.grid[row][i] == 0: 
                return False
        return True

    def clear(self, row):
        for i in range(self.num_cols):
            if self.is_inside(row, i):
                self.grid[row][i] = 0

    def clear_rows(self):
        full_rows = []
        for i in range(self.num_rows - 1, 0, -1):
            if self.is_full(i):
                full_rows.append(i)

        for row in full_rows:
            self.clear(row)
            self.update_rows(row)

        return len(full_rows)

    def update_rows(self, cleared_row):
        for i in range(cleared_row - 1, -1, -1):
            for j in range(self.num_cols):
                if self.is_inside(i, j) and self.grid[i][j] != 0:
                    self.grid[i + 1][j] = self.grid[i][j]
                    self.grid[i][j] = 0

    def draw(self, screen): 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                cell_val = self.grid[i][j]
                cell_rect = pg.Rect(j *self.cellSz + 1, i * self.cellSz + 1, self.cellSz - 1, self.cellSz - 1)
                pg.draw.rect(screen,self.colors[cell_val],cell_rect)



    