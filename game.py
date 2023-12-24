from grid import Grid 
from blocks import * 
import random 
import pygame as pg 

class Game: 
    def __init__(self): 
        self.grid = Grid()
        self.blocks = [Iblock(), Sblock(), Tblock(), Zblock(), Oblock(), Jblock(), Lblock()]
        self.current_block = self.get_rand_block()
        self.next_block = self.get_rand_block()

    def get_rand_block(self): 
        if (len(self.blocks) == 0): 
            self.blocks = [Iblock(), Sblock(), Tblock(), Zblock(), Oblock(), Jblock(), Lblock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)  
        elif self.block_fits() == False:
            self.current_block.move(0,1) 

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)  
        elif self.block_fits() == False:
            self.current_block.move(0,-1) 

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0) 
            self.lock_block()
        elif self.block_fits() == False:
            self.current_block.move(-1, 0) 
            self.lock_block()

    def lock_block(self): 
        tiles = self.current_block.get_pos()
        for position in tiles: 
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_rand_block()
        self.grid.clear_rows()

    def block_fits(self): 
        tiles = self.current_block.get_pos()
        for pos in tiles: 
            if self.grid.is_empty(pos.row, pos.col) == False: 
                return False
        return True 


    def rotate(self): 
        self.current_block.rotate()
        if self.block_inside() == False: 
            self.current_block.undo_rotate()
        elif self.block_fits() == False:
            self.current_block.undo_rotate()

    def block_inside(self):
        tiles = self.current_block.get_pos()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.col) == False:
                return False
        return True

    def draw(self, screen): 
         self.grid.draw(screen)
         self.current_block.draw(screen)