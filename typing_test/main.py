#Typing Tester

from game_funcs import *
from box import *
from paragraph import *
import pygame
import time


pygame.init()
screen = pygame.display.set_mode((1280, 720))

def directions():
    with open('directions.txt') as f:
        text = [i.strip() for i in f.readlines()]

    screen.fill((0, 128, 0))
    for i in text:
        location = (40, (text.index(i) + 1) * 35)
        make_text(i, location, 30, screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

def menu():
    title = 'Typing Test'
    author = 'by: Manny Wang'
    message = 'Press the s key to start.  '
    message += 'Press the d key for directions.'

    screen.fill((0, 128, 0))
    make_text(title, (640, 230), 75, screen, style=True)
    make_text(author, (640, 350), 30, screen, style=True)
    make_text(message, (640, 620), 20, screen, style=True)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.unicode.lower() == 's':
                    countdown(screen)
                    return 's'
                elif event.unicode.lower() == 'd':
                    return 'd'


def game_loop():
    paragraph, text_boxes, user_box = set_up(screen)
    start = time.time()

    while True:
        screen.fill((0, 128, 0))

        wpm = round(calculate_wpm(start, time.time(), paragraph.count))
        time_elapsed = round(time.time() - start)
        accuracy = round(calculate_accuracy(paragraph))

        if is_end(paragraph, paragraph.cur_line):
            show_results(wpm, accuracy, time_elapsed, screen)
            pygame.display.update()
            wait(1)
            return

        update_text_boxes(paragraph, text_boxes, paragraph.cur_line)
        draw_group(text_boxes, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                user_box.evaluate_event(event, paragraph)

        sidebar(wpm, accuracy, time_elapsed, screen)

        user_box.update_text()
        user_box.draw(screen)

        pygame.display.update()

def main():
    while True:
        next = menu()
        if next == 's':
            game_loop()
        elif next == 'd':
            directions()

if __name__ == '__main__':
    main()
