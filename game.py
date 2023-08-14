try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame as pg
    from socket import *
    from pygame.locals import *

    #local imports
    from bat import Bat
    from ball_modified import BallWithPause
    from options import(
        START_PAUSED,
        SCREEN_HEIGTH,
        SCREEN_WIDTH,
        SCREEN_GAME_PERCENTAGE
    )
except (ImportError, Exception) as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)


def main():
    # Initialise screen
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pg.display.set_caption("Duilio's Pong")

    # Fill background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    #Initialize game surface
    game_surface = pg.surface.Surface((SCREEN_WIDTH, int(SCREEN_HEIGTH * SCREEN_GAME_PERCENTAGE)))
    # Initialise players
    global player1
    global player2
    player1 = Bat("left", game_surface)
    player2 = Bat("right", game_surface)

    # Initialise ball
    speed = 13
    rand = ((0.1 * (random.randint(5,8))))
    ball = BallWithPause((0,0),(0.47,speed), game_surface, paused=START_PAUSED)

    # Initialise sprites
    playersprites = pg.sprite.RenderPlain((player1, player2))
    ballsprite = pg.sprite.RenderPlain(ball)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(game_surface, (0, int(SCREEN_HEIGTH * (1 - SCREEN_GAME_PERCENTAGE))))
    pg.display.flip()

    # Initialise clock
    clock = pg.time.Clock()

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pg.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player1.moveup()
                if event.key == K_z:
                    player1.movedown()
                if event.key == K_UP:
                    player2.moveup()
                if event.key == K_DOWN:
                    player2.movedown()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_z:
                    player1.movepos = [0,0]
                    player1.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    player2.movepos = [0,0]
                    player2.state = "still"
                if event.key == K_SPACE:
                    ball.toogle()
                    ball.update(player1, player2)

            #myfont = pg.font.SysFont("monospace", 75)
            #GREEN = (0, 255, 0)
            #label = myfont.render("Tutorial 1", 1, GREEN)
            #screen.blit(label, (0, 10))
            #pg.display.update()
        
        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        ballsprite.update(player1, player2)
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)

        pg.display.flip()


if __name__ == "__main__":
    main()