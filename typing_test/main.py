#Typing Tester

from game_funcs import *
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((1280, 720))

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                return

def game_loop():
    paragraph, text_boxes, user_box = set_up(screen)
    start = time.time()

    while True:
        screen.fill((0, 128, 0))

        wpm = round(calculate_wpm(start, time.time(), paragraph.count))
        time_elapsed = round(time.time() - start)

        if is_end(paragraph, paragraph.cur_line):
            show_results(wpm, time_elapsed, screen)
            pygame.display.update()
            wait()
            return

        update_text_boxes(paragraph, text_boxes, paragraph.cur_line)
        draw_group(text_boxes, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                user_box.evaluate_event(event, paragraph)

        sidebar(wpm, time_elapsed, screen)

        user_box.update_text()
        user_box.draw(screen)

        pygame.display.update()



def main():
    game_loop()

if __name__ == '__main__':
    main()
