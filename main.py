import pygame as pg
import sys 
from game import Game 


# setup game loop and screen 

#initialize pygame 
pg.init()
#rgb colors 
dark_blue = (44,44,127)
red = (255,0,0)

screen = pg.display.set_mode((300,600))
pg.display.set_caption("Tetris")
clock = pg.time.Clock()

GAME_TIME = pg.USEREVENT
pg.time.set_timer(GAME_TIME, 300)

# structure 

# definitions 
    # define objects 
    # create objects

# game loop
    # 1. event handling (pygame event handling)
    # 2. update positions (based on events before)
    # 3. check collisions (draw game objects on screen)
game = Game()

while True: 
    # gets events that pg recognizes 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()
        
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_LEFT: 
                game.move_left()
            if event.key == pg.K_RIGHT: 
                game.move_right()
            if event.key == pg.K_UP: 
                game.rotate()
            if event.key == pg.K_DOWN: 
                game.move_down()
        if event.type == GAME_TIME: 
            game.move_down()

                
    # drawing 
    screen.fill(dark_blue)
    game.draw(screen)
    pg.display.update()
    # uncomment for debugging 
    # game.grid.print_grid()

    # runs 60 frames/ second 
    clock.tick(60)
