#Typing Tester

from game_funcs import *
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((1280, 720))

def game_loop():
    paragraph, text_boxes, user_box = set_up(screen)

    while True:
        screen.fill((0, 128, 0))

        if is_end(paragraph, paragraph.cur_line):
            return
        update_text_boxes(paragraph, text_boxes, paragraph.cur_line)
        draw_group(text_boxes, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                user_box.evaluate_event(event, paragraph)

        user_box.update_text()
        user_box.draw(screen)

        pygame.display.update()


def main():
    game_loop()

if __name__ == '__main__':
    main()
