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
