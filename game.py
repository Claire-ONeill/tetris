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
        self.held_block = None
        self.has_held_block = False
        self.holding_block = False
        self.GameOver = False
        self.score = 0
        self.level = 1
        self.lines = 0 
        self.command = 0

    def update_score(self, rows_clear, points): 
        # update lines cleared 
        self.lines += rows_clear 
        points = 0 
        multiplier = 1
        bonus = 0.1  
        if rows_clear == 1: 
            points += 100
        elif rows_clear == 2: 
            points += 300
        elif rows_clear == 3: 
            points += 500 
        else: 
            points += 800
        # set level: raise level every 5k points until level 25 is hit 
            # multiplier cap 0.1*25 = 2.5x 
        if self.level < 25 and self.score + points >= 1000: 
             self.level = int(self.score//1000)
             if self.score >= 5000: 
                bonus *= int(self.score//5000) 
                points *= (multiplier + bonus)
        
        self.score += points 


    def get_rand_block(self): 
        if (len(self.blocks) == 0): 
            self.blocks = [Iblock(), Sblock(), Tblock(), Zblock(), Oblock(), Jblock(), Lblock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)  
        # elif self.block_fits() == False:
        #     self.current_block.move(0,1) 

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)  
        # elif self.block_fits() == False:
        #     self.current_block.move(0,-1) 

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()
        # elif not self.block_fits():
        #     self.current_block.move(-1, 0)
        #     self.lock_block()
        #     if not self.block_fits():
        #         self.GameOver = True
    
    def move_bottom(self): 
        while self.block_inside() and self.block_fits(): 
            self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_block()
            return 
        self.lock_block()


    def lock_block(self):
        tiles = self.current_block.get_pos()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        cleared = self.grid.clear_rows()  # Clear rows before updating to the next block
        self.current_block = self.next_block
        self.next_block = self.get_rand_block()
        if cleared > 0: 
            self.update_score(cleared, 0)
        if not self.block_fits(): 
            self.GameOver = True 

    def reset(self): 
        self.grid.reset()
        self.blocks = [Iblock(), Sblock(), Tblock(), Zblock(), Oblock(), Jblock(), Lblock()]
        self.current_block = self.get_rand_block()
        self.next_block = self.get_rand_block()
        self.hold_block = None
        self.has_held_block = False
        self.holding_block = False
        self.score = 0
        self.command = 0 

    def block_fits(self): 
        tiles = self.current_block.get_pos()
        for pos in tiles: 
            if not self.grid.is_empty(pos.row, pos.col): 
                return False
        return True 


    def rotate(self): 
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits(): 
            self.current_block.undo_rotate()
        # elif self.block_fits() == False:
        #     self.current_block.undo_rotate()

    def block_inside(self):
        tiles = self.current_block.get_pos()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True
    
    def hold_block(self): 
        if not self.holding_block: 
            if not self.held_block:  
                self.held_block = self.current_block
                self.current_block = self.next_block
                self.next_block = self.get_rand_block()
            else: 
                temp_block = self.held_block
                self.held_block = self.current_block
                self.current_block = temp_block
            self.has_held_block = True
            self.holding_block = True 
        else: 
            temp = self.held_block
            self.held_block = self.current_block
            self.current_block = temp 
        

    def draw(self, screen): 
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        # draw held block if applicable 
        # if self.holding_block and self.held_block: 
        #     if self.held_block.id == 3: 
        #         self.held_block.draw(screen, 255, 220)
        #     elif self.held_block.id == 4: 
        #         self.held_block.draw(screen, 250, 220)
        #     else: 
        #         self.held_block.draw(screen, 270, 220)
        # draw next block 
        if self.next_block.id == 3: 
            self.next_block.draw(screen, 255, 70)
        elif self.next_block == 4: 
            self.next_block.draw(screen, 250, 70)
        else: 
            self.next_block.draw(screen, 270, 70)