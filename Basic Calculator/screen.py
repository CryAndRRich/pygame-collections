import pygame
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (140, 140, 140)
LIGHT_GRAY = (241, 243, 244)
DARK_GRAY = (218, 220, 224)
BLUE = (66, 133, 244)

BACKGROUND = pygame.image.load('background.jpg')

font1 = pygame.font.SysFont('consolas', 30)
font2 = pygame.font.SysFont('consolas', 16)
font3 = pygame.font.SysFont('arial bold', 22)

class CalculatorScreen:
    def __init__(self, surface):
        self.surface = surface
        self.input_text = ''
        self.result_text = ''
        self.equal_buttons = False
        self.is_radian = True
        self.buttons = []
        self.operate = {0: 'Rad', 1: 'x!', 2: '(', 3: ')', 4: '%', 5: 'CE', 
                        6: 'e', 7: '1/x', 8: '7', 9: '8', 10: '9', 11: '/', 
                        12: 'sin', 13: 'ln', 14: '4', 15: '5', 16: '6', 17: 'x', 
                        18: 'cos', 19: 'log', 20: '1', 21: '2', 22: '3', 23: '-', 
                        24: 'tan', 25: '^', 26: '0', 27: '.', 28: '=', 29: '+'}
        self.button_color = [DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY, DARK_GRAY, 
                             DARK_GRAY, DARK_GRAY, LIGHT_GRAY, LIGHT_GRAY, BLUE, DARK_GRAY]
        for i in range(0, 5):
            for j in range(0, 6):
                self.buttons.append(pygame.Rect(105 + 100 * j, 140 + 45 * i, 87, 28))

    def handle_click(self, pos):
        for i, button_rect in enumerate(self.buttons):
            if button_rect.collidepoint(pos):
                if self.operate[5] == 'AC':
                    if i not in [0, 1, 4, 11, 17, 23, 25, 28, 29]:
                        self.result_text = ''
                    if i != 0:
                        self.operate[5] = 'CE'

                if i == 5:
                    self.result_text = self.result_text[:-1] if self.operate[5] == 'CE' else ''
                elif i == 28:
                    self.equal_buttons = True
                    self.operate[5] = 'AC'
                elif i == 1:
                    self.result_text += '!'
                elif i == 7:
                    self.result_text += '1/'
                elif i == 0:
                    self.operate[0] = 'Deg' if self.is_radian else 'Rad'
                    self.is_radian = not self.is_radian
                else:
                    self.result_text += self.operate[i]
                    if i in [12, 13, 18, 19, 24]:
                        self.result_text += '('
        
                return  

    def draw_buttons(self):
        for i, button_rect in enumerate(self.buttons):
            pygame.draw.rect(self.surface, self.button_color[i], button_rect)
            text = self.operate[i]
            text_surface = font3.render(text, True, WHITE if i == 28 else BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.surface.blit(text_surface, text_rect)

    def draw_frame(self):
        frame = pygame.Rect(105, 60, 587, 65)
        pygame.draw.rect(self.surface, WHITE, frame)

        text_surface_input = font2.render(self.input_text, True, GRAY)
        text_surface_result = font1.render(self.result_text, True, BLACK)
        
        text_rect_input = text_surface_input.get_rect(top=frame.top + 10, right=frame.right - 10)
        text_rect_result = text_surface_result.get_rect(bottom=frame.bottom - 5, right=frame.right - 10)

        self.surface.blit(text_surface_input, text_rect_input)
        self.surface.blit(text_surface_result, text_rect_result)

    def update_display(self):
        self.surface.blit(BACKGROUND, (0, 0))
        self.draw_buttons()
        self.draw_frame()
