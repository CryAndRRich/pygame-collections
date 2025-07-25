import pygame
import sys
from pygame.locals import *
from screen import CalculatorScreen
from utils import Calculate

pygame.init()

def CalculatorApp():
    DISPLAYSURF = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Basic Calculator')

    screen = CalculatorScreen(DISPLAYSURF)  

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                screen.handle_click(event.pos)
                if len(screen.result_text) > 32:
                    screen.result_text = 'Stop! Too long!'
                    screen.operate[5] = 'AC'
                if screen.equal_buttons: 
                    try:
                        screen.input_text = screen.result_text + '='
                        screen.result_text = f'{Calculate(screen.result_text, screen.is_radian)}'
                        if len(screen.result_text) > 32:
                            screen.result_text = 'Sorry! Too long!'
                    except:
                        screen.result_text = 'ERROR'
                    
                    screen.equal_buttons = False
            
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                elif event.key == pygame.K_BACKSPACE:  
                    screen.result_text = screen.result_text[:-1]
                elif event.key == pygame.K_DELETE:
                    screen.result_text = ''
                    screen.operate[5] = 'AC'
                elif event.key == pygame.K_RETURN: 
                    screen.input_text = screen.result_text + '='
                    try:
                        screen.result_text = f'{Calculate(screen.result_text, screen.is_radian)}'
                    except:
                        screen.result_text = 'ERROR'
                else:
                    key = event.unicode
                    if key in "0123456789+-x/%^().!e": 
                        screen.result_text += key
                    elif key in "sct":
                        tri = {'s': 'sin', 'c': 'cos', 't': 'tan'}
                        screen.result_text += tri[key] + '('
                    elif key == 'l':
                        screen.result_text += key
                    elif key in 'on':
                        screen.result_text += key + ('g' if key == 'o' else '') + '('

                if len(screen.result_text) > 32:  
                    screen.result_text = 'Stop! Too long!'
                    screen.operate[5] = 'AC'

            screen.update_display()
            pygame.display.update()

if __name__ == '__main__':
    CalculatorApp()
