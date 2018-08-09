#Game functions for typing_test

from paragraph import *
from line import *


def set_up(screen):
    paragraph = Paragraph()

    height = 50
    locations = calculate_locations(screen)
    text_boxes = tuple(TextBox(height) for i in range(4))
    for text_box, location in zip(text_boxes, locations[:-1]):
        text_box.move(location)

    user_box = UserBox(height)
    user_box.move(locations[-1])
    user_box.color_swap()

    return paragraph, text_boxes, user_box

def calc_lines_left(paragraph, current_line):
    return len(paragraph.lines) - current_line

def is_end(paragraph, current_line):
    lines_left = calc_lines_left(paragraph, current_line)
    if lines_left == 0:
        return True

def update_text_boxes(paragraph, text_boxes, current_line):
    lines_left = calc_lines_left(paragraph, current_line)
    text_lines = paragraph.lines[current_line:current_line + lines_left]
    while len(text_lines) < 4:
        text_lines.append(None)

    for i, j in zip(text_boxes, text_lines):
        i.update_text(j)

def calculate_wpm(start, now, count):
    time = round(now - start) / 60
    if count == 0:
        return 0
    return (count / 5) / time

def sidebar(wpm, time_elapsed, screen):
    font = pygame.font.SysFont('Arial', 20)
    color = (255, 255, 255)

    wpm_surf = font.render('Wpm: {}'.format(wpm), False, color)
    time_surf = font.render('Time Passed: {}'.format(time_elapsed), False, color)

    screen.blit(wpm_surf, (0, 0))
    screen.blit(time_surf, (0, 30))

def show_results(wpm, time_elapsed, screen):
    wpm_font = pygame.font.SysFont('Arial', 50)
    message_font = pygame.font.SysFont('Arial', 20)
    color = (255, 255, 255)

    wpm_surf = wpm_font.render('Your final wpm was {}.'.format(wpm), False, color)
    wpm_rect = wpm_surf.get_rect(center=(640, 360))
    message_surf = message_font.render('Press any key to continue.', False, color)
    message_rect = message_surf.get_rect(center=(640, 560))
    screen.blit(wpm_surf, wpm_rect)
    screen.blit(message_surf, message_rect)
