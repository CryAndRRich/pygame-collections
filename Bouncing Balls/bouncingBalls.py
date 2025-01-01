import pygame
import sys
from gamePlay import gamePlay

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bouncing Balls')

FPS = 60
fpsClock = pygame.time.Clock()

BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

def Bouncing_Balls():
    play = gamePlay(WINDOW_WIDTH, WINDOW_HEIGHT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        play.start_angle += play.spinning_speed
        play.end_angle += play.spinning_speed

        play.check_collisions()

        DISPLAYSURF.fill(BLACK)
        pygame.draw.circle(DISPLAYSURF, ORANGE, play.circle_center, play.circle_radius, 3)
        play.draw(DISPLAYSURF)

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    Bouncing_Balls()

