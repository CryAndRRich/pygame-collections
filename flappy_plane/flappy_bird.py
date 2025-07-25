import pygame, sys, random
from pygame.locals import *

pygame.mixer.init()
pygame.init()

#tạo khung
window_width = 400
window_height = 600
#thêm ảnh con chim
bird_width = 60
bird_height = 45
G = 0.5
speed_fly = -7
bird_img = pygame.image.load('plane.png')
#thêm ảnh cột
column_width = 60
column_height = 500
BLANK = 160
DISTANCE = 200
column_speed = 1.5
column_img = pygame.image.load('tower.png')
#thêm background
BACKGROUND = pygame.image.load('manhattan.png')
#thêm âm thanh
sound_background=pygame.mixer.Sound('Osama.wav')
sound_end=pygame.mixer.Sound('kaboom.wav')

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird - 911v')
#hàm chuyển động của chim
class Bird():
    def __init__(self):
        self.width = bird_width
        self.height = bird_height
        self.x = (window_width - self.width)/2
        self.y = (window_height- self.height)/2
        self.speed = 0
        self.surface = bird_img
    #vị trí của chim so với khung
    def draw(self):
        DISPLAYSURF.blit(self.surface, (int(self.x), int(self.y)))
    #tốc độ bay
    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G
        if mouseClick == True:
            self.speed = speed_fly
#hàm của cột
class Columns():
    def __init__(self):
        self.width = column_width
        self.height = column_height
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = column_speed
        self.surface = column_img
    
        self.ls = []
        for i in range(3):
            x = window_width + i*self.distance
            y = random.randrange(60, window_height - self.blank - 60, 20)
            self.ls.append([x, y])
        
    def draw(self):
        for i in range(3):
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] - self.height))
            DISPLAYSURF.blit(self.surface, (self.ls[i][0], self.ls[i][1] + self.blank))
    
    def update(self):
        for i in range(3):
            self.ls[i][0] -= self.speed
        
        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = random.randrange(60, window_height - self.blank - 60, 10)
            self.ls.append([x, y])
#hàm xét sự va chạm của chim với cột
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False
#hàm xét khi nào trò chơi kết thúc
def isGameOver(bird, columns):
    for i in range(3):
        rectBird = [bird.x, bird.y, bird.width, bird.height]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > window_height:
        return True
    return False
#hàm tính điểm
class Score():
    def __init__(self):
        self.score = 0
        self.addScore = True
    
    def draw(self):
        font = pygame.font.SysFont('consolas', 40)
        scoreSurface = font.render(str(self.score), True, (0, 0, 0))
        textSize = scoreSurface.get_size()
        DISPLAYSURF.blit(scoreSurface, (int((window_width - textSize[0])/2), 100))
    
    def update(self, bird, columns):
        collision = False
        for i in range(3):
            rectColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            rectBird = [bird.x, bird.y, bird.width, bird.height]
            if rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += random.randint(100,1000)
            self.addScore = False
        else:
            self.addScore = True
#hàm tạo màn hình khởi đầu
def gameStart(bird):
    bird.__init__()

    font = pygame.font.SysFont('consolas', 50)
    headingSurface = font.render('FLAPPY PLANE', True, (255, 0, 0))
    headingSize = headingSurface.get_size()
    
    font = pygame.font.SysFont('consolas', 20)
    commentSurface = font.render('Click to start', True, (0, 0, 0))
    commentSize = commentSurface.get_size()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                sound_background.play(loops=100)
                return

        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        bird.draw()
        DISPLAYSURF.blit(headingSurface, (int((window_width - headingSize[0])/2), 100))
        DISPLAYSURF.blit(commentSurface, (int((window_width - commentSize[0])/2), 500))

        pygame.display.update()
        fpsClock.tick(FPS)
#hàm diễn biến trò chơi
def gamePlay(bird, columns, score):
    bird.__init__()
    bird.speed = speed_fly
    columns.__init__()
    score.__init__()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        columns.draw()
        columns.update()
        bird.draw()
        bird.update(mouseClick)
        score.draw()
        score.update(bird, columns)
        if isGameOver(bird, columns) == True:
            sound_background.stop()
            sound_end.play()
            return
        pygame.display.update()
        fpsClock.tick(FPS)
#hàm tạo màn hình kết thúc
def gameOver(bird, columns, score):
    font = pygame.font.SysFont('consolas', 60)
    headingSurface = font.render('YOU DIED', True, (255, 0, 0))
    headingSize = headingSurface.get_size()
    
    font = pygame.font.SysFont('consolas', 20)
    commentSurface = font.render('Press "space" to replay', True, (0, 0, 0))
    commentSize = commentSurface.get_size()

    font = pygame.font.SysFont('consolas', 30)
    scoreSurface = font.render('PEOPLE SAVED: ' + str(score.score), True, (0, 0, 0))
    scoreSize = scoreSurface.get_size()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    sound_end.stop()
                    return
        
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        columns.draw()
        bird.draw()
        DISPLAYSURF.blit(headingSurface, (int((window_width - headingSize[0])/2), 100))
        DISPLAYSURF.blit(commentSurface, (int((window_width - commentSize[0])/2), 500))
        DISPLAYSURF.blit(scoreSurface, (int((window_width - scoreSize[0])/2), 160))

        pygame.display.update()
        fpsClock.tick(FPS)

def main():
    bird = Bird()
    columns = Columns()
    score = Score()
    while True:
        gameStart(bird)
        gamePlay(bird, columns, score)
        gameOver(bird, columns, score)

if __name__ == '__main__':
    main()