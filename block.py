from colors import Colors 
import pygame as pg
from position import Position 


class Block: 
    def __init__(self, id): 
        self.id = id
        self.cells = {}
        self.cell_sz = 30
        self.rotationState = 0
        self.row_off = 0
        self.col_off = 0 
        self.holding_block = False 
        self.colors = Colors.get_colors()
    
    def move(self, rows, cols): 
        self.row_off += rows
        self.col_off += cols 

    def get_pos(self): 
        tiles = self.cells[self.rotationState]
        moved_tiles = []
        for pos in tiles: 
            pos = Position(pos.row + self.row_off, pos.col + self.col_off) 
            moved_tiles.append(pos)
        return moved_tiles 
    
    def rotate(self): 
        self.rotationState += 1
        if self.rotationState == len(self.cells): 
            self.rotationState = 0 
    
    def undo_rotate(self): 
        self.rotationState -= 1
        if self.rotationState == -1:
            self.rotationState = len(self.cells) - 1
    
    def draw(self,screen, x_off, y_off):
        tiles = self.get_pos()
        for tile in tiles: 
            tile_rect = pg.Rect(tile.col * self.cell_sz + x_off, 
                                tile.row * self.cell_sz + y_off, 
                                self.cell_sz - 1 , self.cell_sz - 1)
            pg.draw.rect(screen, self.colors[self.id], tile_rect)