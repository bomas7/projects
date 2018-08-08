import pygame


pygame.font.init()

class Line:

    def __init__(self, height, color=(255, 255, 255)):

        self.text = None
        self.text_surf = None
        self.text_rect = None
        self.text_color = color
        self.text_font = pygame.font.SysFont('Arial', int(height*.85))

        self.rect = pygame.Rect(0, 0, height * 17.3, height)
        self.rect_color = tuple(i - j for i, j in zip((255, 255, 255), color))

    def update_text(self, text):
        self.text = text
        self.text_surf = self.text_font.render(self.text, False, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def move(self, location):
        x, y = location
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.rect)
        screen.blit(self.text_surf, self.text_rect)


class UserLine(Line):

    def color_swap(self):
        self.text_color, self.rect_color = self.rect_color, self.text_color


def calculate_locations(screen):
    h = screen.get_height()
    locations = []
    for i in range(1, 6):
        locations.append((screen.get_width() // 2, i * h // 7))
    return locations
