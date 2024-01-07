import pygame as pg
import sys 
from game import Game 
from colors import Colors

# setup game loop and screen 

#initialize pygame 
pg.init()

# title screen 
titleFont = pg.font.Font(None, 40)
score_lay = titleFont.render("Score", True, Colors.white)
next_lay = titleFont.render("Next", True, Colors.white)
game_over = titleFont.render("GAME OVER", True, Colors.white)

score_box = pg.Rect(320, 55, 170, 60)
next_box = pg.Rect(320, 215, 170, 180)

screen = pg.display.set_mode((500, 620))
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
            if game.GameOver: 
                game.GameOver = False
                game.reset() 
            if event.key == pg.K_LEFT and not game.GameOver: 
                game.move_left()
            if event.key == pg.K_RIGHT and not game.GameOver: 
                game.move_right()
            if event.key == pg.K_UP and not game.GameOver: 
                game.rotate()
            if event.key == pg.K_DOWN and not game.GameOver: 
                game.move_down()
            if event.key == pg.K_SPACE and not game.GameOver: 
                game.move_bottom()
        if event.type == GAME_TIME and not game.GameOver: 
            game.move_down()

                
    # drawing 
    score_val_lay = titleFont.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_lay, (365, 20, 50, 50))
    screen.blit(next_lay, (375, 180, 50, 50))

    if game.GameOver: 
        screen.blit(game_over, (320, 450, 50, 50))
    
    pg.draw.rect(screen, Colors.light_blue, score_box, 0, 10)
    screen.blit(score_val_lay, score_val_lay.get_rect(centerx = score_box.centerx, centery = score_box.centery))
    pg.draw.rect(screen, Colors.light_blue, next_box, 0, 10)
    game.draw(screen)
    pg.display.update()
    # uncomment for debugging 
    # game.grid.print_grid()

    # runs 60 frames/ second 
    clock.tick(60)
