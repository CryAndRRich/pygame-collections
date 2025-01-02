import time
import sys
from constants import *
from gamePlay import gamePlay

def main():
    game = gamePlay()
    game.fill_objects()
    ticks = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in {pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN}:
                DISPLAYSURF.fill(BLACK)
                game.clear_objects()
                ticks = 0
                pygame.display.flip()
                time.sleep(1 / FPS)
                game.fill_objects()

        game.update(ticks)
        ticks += 1
        game.draw_text()
        
        time.sleep(1 / FPS)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
