#Typing Tester

from game_funcs import *
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((1280, 720))

def game_loop():
    text, lines, user_line = set_up(screen)
    user_input = ''
    current_line = 0

    while True:
        screen.fill((0, 128, 0))
        update_line_text(text, lines, current_line)

        #draw lines
        for line in lines:
            line.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    user_input = ''
                elif event.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isalpha() or event.unicode.isdigit():
                    user_input += event.unicode

        user_line.update_text(user_input)
        user_line.draw(screen)

        pygame.display.update()





def main():
    game_loop()

if __name__ == '__main__':
    main()
