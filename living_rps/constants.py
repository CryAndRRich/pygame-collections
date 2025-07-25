import pygame

pygame.mixer.init()
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption('Rock Paper Scissors')

FONT = pygame.font.SysFont('consolas', 18)

SOUND_COLLIDE = pygame.mixer.Sound('collide.mp3')
SOUND_APPEAR = pygame.mixer.Sound('appear.mp3')
SOUND_COLLIDE.set_volume(0.5)
SOUND_APPEAR.set_volume(0.2)

RADIUS = 12
ROCK_IMG = pygame.transform.scale(pygame.image.load("rock.png"), (RADIUS * 2, RADIUS * 2))
PAPER_IMG = pygame.transform.scale(pygame.image.load("paper.png"), (RADIUS * 2, RADIUS * 2))
SCISSORS_IMG = pygame.transform.scale(pygame.image.load("scissors.png"), (RADIUS * 2, RADIUS * 2))

CHOICES = {0: ROCK_IMG, 1: PAPER_IMG, 2: SCISSORS_IMG}
WIN_RULES = {0: 2, 1: 0, 2: 1}

MAX_VEL = 2
MAX_ACCEL = 2

FPS = 80
fpsClock = pygame.time.Clock()
