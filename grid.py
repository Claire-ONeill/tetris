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
        if 0 <= row and row < self.num_rows and 0 <= column and column < self.num_cols:
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
            # if self.is_inside(row, i):
            self.grid[row][i] = 0
    
    def clear_rows(self): 
        complete = 0
        for i in range(self.num_rows - 1, 0, -1): 
            if self.is_full(i): 
                self.clear(i)
                complete += 1
            elif complete > 0: 
                self.update_rows(i, complete)
        return complete 

    # def clear_rows(self):
    #     full_rows = []
    #     for i in range(self.num_rows - 1, 0, -1):
    #         if self.is_full(i):
    #             full_rows.append(i)

    #     for row in full_rows:
    #         self.clear(row)
    #         self.update_rows(row)

    #     return len(full_rows)

    def update_rows(self, row, cleared_row):
        for j in range(self.num_cols): 
            self.grid[row + cleared_row][j] = self.grid[row][j]
            self.grid[row][j] = 0 
        # for i in range(cleared_row - 1, 0, -1):
        #     for j in range(self.num_cols):
        #         if self.is_inside(i, j):
        #             self.grid[i + 1][j] = self.grid[i][j]
        #             self.grid[i][j] = 0
            
    def reset(self): 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                self.grid[i][j] = 0 

    def draw(self, screen): 
        for i in range(self.num_rows): 
            for j in range(self.num_cols): 
                cell_val = self.grid[i][j]
                cell_rect = pg.Rect(j *self.cellSz + 11, i * self.cellSz + 11, self.cellSz - 1, self.cellSz - 1)
                pg.draw.rect(screen,self.colors[cell_val],cell_rect)



    