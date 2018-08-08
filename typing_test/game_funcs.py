#Game functions for typing_test

from paragraph import *
from line import *


def set_up(screen):
    text = Paragraph()

    height = 50
    locations = calculate_locations(screen)
    lines = tuple(Line(height) for i in range(4))
    for line, location in zip(lines, locations[:-1]):
        line.move(location)

    user_line = UserLine(height)
    user_line.move(locations[-1])
    user_line.color_swap()

    return text, lines, user_line

def update_line_text(text, lines, current_line):
    text_lines = text.lines[current_line:current_line + 4]
    for i, j in zip(lines, text_lines):
        i.update_text(j)
    return lines
