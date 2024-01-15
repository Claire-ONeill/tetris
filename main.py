import asyncio 
import pygame as pg
import sys 
from game import Game 
from colors import Colors

async def main(): 
    # setup game loop and screen 

    #initialize pygame 
    pg.init()

    # title screen 
    titleFont = pg.font.Font(None, 40)
    statsFont = pg.font.Font(None, 30)
    instructionsFont = pg.font.Font(None, 20)
    score_lay = statsFont.render("Score", True, Colors.white)
    next_lay = titleFont.render("Next", True, Colors.white)
    # game_over = titleFont.render("GAME OVER", True, Colors.white)

    score_box = pg.Rect(320, 330, 170, 280)
    next_box = pg.Rect(320, 10, 170, 150)
    hold_box = pg.Rect(320, 170, 170, 150)
    score_item1 = pg.Rect(330, 365, 150, 50)
    score_item2 = pg.Rect(330, 460, 150, 50)
    score_item3 = pg.Rect(330, 550, 150, 50)

    game_over_box = pg.Rect(120, 200, 260, 200)
    curr_score = pg.Rect(130, 300, 240, 50)

    screen = pg.display.set_mode((500, 620))
    pg.display.set_caption("Tetris")
    clock = pg.time.Clock()

    SPEED = 300
    GAME_TIME = pg.USEREVENT
    pg.time.set_timer(GAME_TIME, SPEED)

    # structure 

    # definitions 
        # define objects 
        # create objects

    # game loop
        # 1. event handling (pygame event handling)
        # 2. update positions (based on events before)
        # 3. check collisions (draw game objects on screen)
    game = Game()
    command = ''

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
                    game.command = 0
                if event.key == pg.K_RIGHT and not game.GameOver: 
                    game.move_right()
                    game.command = 0
                if event.key == pg.K_UP and not game.GameOver: 
                    game.rotate()
                    game.command = 0
                if event.key == pg.K_DOWN and not game.GameOver: 
                    game.move_down()
                    game.command = 0
                if event.key == pg.K_SPACE  and not game.GameOver: 
                    game.move_bottom()
                    game.command = 0
                if event.key == pg.K_c and not game.GameOver: 
                    game.hold_block()
                    game.command = 1
            # if command not hold move game
            if event.type == GAME_TIME and not game.GameOver: 
                faster = 10 
                if game.level >= 5: 
                    new_speed = SPEED - (10 * (game.level//5))
                    pg.time.set_timer(GAME_TIME, SPEED)
                game.move_down()
                    
        # drawing 
        score_val_lay = titleFont.render(str(game.score), True, Colors.white)
        screen.fill(Colors.dark_blue)
        screen.blit(score_lay, (365, 20, 50, 50))
        screen.blit(next_lay, (375, 180, 50, 50))

        # if game.GameOver: 
        #     game_over_text = titleFont.render("Game Over", True, Colors.white)
        #     pg.draw.rect(screen, Colors.dark_grey, game_over_box, 0, border_radius=10)
        #     pg.draw.rect(screen, Colors.white, game_over_box, 1, border_radius=10)
        #     screen.blit(game_over_text, (200, 250))  # Adjust the position
        screen.fill(Colors.dark_blue)

        # Draw the "Next" box
        pg.draw.rect(screen, Colors.dark_grey, next_box, 0, border_radius=10)
        pg.draw.rect(screen, Colors.white, next_box, 1, border_radius=10) 
        next_text = titleFont.render("Next", True, Colors.white)
        screen.blit(next_text, (370, 25)) 

#  In the works still buggy 
        # Draw the "Hold" box
        # pg.draw.rect(screen, Colors.dark_grey, hold_box, 0, border_radius=10)
        # pg.draw.rect(screen, Colors.white, hold_box, 1, border_radius=10) 
        # hold_text = titleFont.render("Hold", True, Colors.white)
        # screen.blit(hold_text, (370, 180)) 

        # Draw the "stats" box
        pg.draw.rect(screen, Colors.dark_grey, score_box, 0, border_radius=10)
        pg.draw.rect(screen, Colors.white, score_box, 1, border_radius=10) 

        # score box
        score_text = statsFont.render("Score", True, Colors.white)
        score_val_text = statsFont.render(str(game.score), True, Colors.white)
        screen.blit(score_text, (370, 340))  
        pg.draw.rect(screen, Colors.dark_blue, score_item1, 0, border_radius=10)
        pg.draw.rect(screen, Colors.white, score_item1, 1, border_radius=10)
        screen.blit(score_val_text, (390, 380))  

        # lines cleared box 
        level_text = statsFont.render("Level", True, Colors.white)
        level_val_text = statsFont.render(str(game.level), True, Colors.white)
        screen.blit(level_text, (370, 430))  
        pg.draw.rect(screen, Colors.dark_blue, score_item2, 0, border_radius=10)
        pg.draw.rect(screen, Colors.white, score_item2, 1, border_radius=10)
        screen.blit(level_val_text, (390, 475)) 
        
        # level box 
        lines_text = statsFont.render("Lines Cleared", True, Colors.white)
        lines_val_text = statsFont.render(str(game.lines), True, Colors.white)
        screen.blit(lines_text, (335, 520))  
        pg.draw.rect(screen, Colors.dark_blue, score_item3, 0, border_radius=10)
        pg.draw.rect(screen, Colors.white, score_item3, 1, border_radius=10)
        screen.blit(lines_val_text, (390, 560))  

        game.draw(screen)
    
        if game.GameOver: 
            game_over_text = titleFont.render("GAME OVER", True, Colors.white)
            pg.draw.rect(screen, Colors.dark_grey, game_over_box, 0, border_radius=10)
            pg.draw.rect(screen, Colors.white, game_over_box, 1, border_radius=10)
            screen.blit(game_over_text, (165, 220)) 
  
            pg.draw.rect(screen, Colors.dark_blue, curr_score, 0, border_radius=10)
            pg.draw.rect(screen, Colors.white, curr_score, 1, border_radius=10)
            end_score = statsFont.render("Final Score", True, Colors.white)
            screen.blit(end_score, (190, 270))
            final_score = statsFont.render(str(game.score), True, Colors.white)
            screen.blit(final_score, (240, 310))
            end_score = instructionsFont.render("press the space bar to continue", True, Colors.white)
            screen.blit(end_score, (145, 360))

        await asyncio.sleep(0)
        pg.display.update()
        clock.tick(60)

# run main loop
asyncio.run(main())
