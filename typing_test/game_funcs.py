#Game functions for typing_test

from paragraph import *
from box import *
import time
import pygame

#General

def set_up(screen):
    paragraph = Paragraph()

    height = 50
    locations = calculate_locations(screen)
    text_boxes = tuple(TextBox(height) for i in range(4))
    for text_box, location in zip(text_boxes, locations[:-1]):
        text_box.move(location)

    user_box = UserBox(height)
    user_box.move(locations[-1])

    return paragraph, text_boxes, user_box

def draw_group(group, screen):
    for i in group:
        i.draw(screen)

def is_end(paragraph, current_line):
    lines_left = len(paragraph.lines) - current_line
    if lines_left == 0:
        return True

def update_text_boxes(paragraph, text_boxes, current_line):
    lines_left = len(paragraph.lines) - current_line
    text_lines = paragraph.lines[current_line:current_line + lines_left]
    while len(text_lines) < 4:
        text_lines.append(None)

    for i, j in zip(text_boxes, text_lines):
        i.update_text(j)

def wait(delay=0):
    while True:
        time.sleep(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                return

def countdown(screen):
    for i in (3, 2, 1):
        screen.fill((0, 128, 0))
        make_text(str(i), (640, 360), 50, screen, style=True)
        pygame.display.update()
        time.sleep(1)
        
#Calculations

def calculate_locations(screen):
    h = screen.get_height()
    locations = []
    for i in range(1, 6):
        locations.append((screen.get_width() // 2, i * h // 7))
    return locations

def calculate_wpm(start, now, count):
    if count == 0:
        return 0
    time = round(now - start) / 60
    return (count / 5) / time

def calculate_accuracy(paragraph):
    if paragraph.errors == 0 and paragraph.count > 0:
        return 100
    elif paragraph.count == 0:
        return 0
    else:
        return (paragraph.count - paragraph.errors) / paragraph.count * 100

#Text Display

def make_text(text, location, size, screen, color=(255, 255, 255), style=False):
    font = pygame.font.SysFont('Arial', size)
    text_surf = font.render(text, False, color)
    if style == True:
        location = text_surf.get_rect(center=location)
    screen.blit(text_surf, location)

def make_batch(texts, locations, size, screen, color=(255, 255, 255), style=False):
    for i, j in zip(texts, locations):
        make_text(i, j, size, screen, color, style)

def sidebar(wpm, accuracy, time_elapsed, screen):
    texts = [
        'Wpm: {}'.format(wpm),
        'Accuracy: {}'.format(accuracy),
        #'Time Elapsed: {}'.format(time_elapsed)
    ]

    #locations = [(0, 0), (0, 30), (0, 60)]
    locations = [(0, 0), (0, 30)]
    make_batch(texts, locations, 20, screen)

def show_results(wpm, accuracy, time_elapsed, screen):
    texts = [
        'Your wpm was: {}'.format(wpm),
        'Your accuracy was {}%'.format(accuracy),
        'Total time: {} seconds'.format(time_elapsed)
    ]

    locations = [(640, 250), (640, 310), (640, 370)]
    make_batch(texts, locations, 35, screen, style=True)

    message = 'Press any key to continue'
    message_location = (640, 600)
    make_text(message, message_location, 20, screen, style=True)
