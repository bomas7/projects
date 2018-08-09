import pygame


pygame.font.init()

class TextBox:

    def __init__(self, height, color=(255, 255, 255)):

        self.text = None
        self.text_surf = None
        self.text_rect = None
        self.text_color = color
        self.text_font = pygame.font.SysFont('Arial', int(height*.85))

        self.rect = pygame.Rect(0, 0, height * 17.3, height)
        self.rect_color = tuple(i - j for i, j in zip((255, 255, 255), color))

    def update_text(self, text):
        if text == False:
            self.text_surf = None
            self.text_rect = None
            return
        self.text = text
        self.text_surf = self.text_font.render(self.text, False, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def move(self, location):
        x, y = location
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.rect)
        if self.text_surf and self.text_rect:
            screen.blit(self.text_surf, self.text_rect)


class UserBox(TextBox):

    def __init__(self, height, color=(255, 255, 255)):
        TextBox.__init__(self, height, color)
        self.text_color, self.rect_color = self.rect_color, self.text_color
        self.input = ''

    def update_text(self):
        TextBox.update_text(self, text=self.input)

    def box_color(self, paragraph):
        word_compare = paragraph.cur_word[:len(self.input)]
        if self.input != word_compare or len(self.input) > len(paragraph.cur_word):
            self.rect_color = (255, 0 ,0)
            paragraph.errors += 1
        else:
            self.rect_color = (255, 255, 255)

    def evaluate_event(self, event, paragraph):
        if event.key == pygame.K_SPACE:
            if self.input == paragraph.cur_word:
                paragraph.status_update()
                self.input = ''

        elif event.key == pygame.K_BACKSPACE:
            self.input = self.input[:-1]

        elif event.unicode.isalpha() or event.unicode.isdigit():
            self.input += event.unicode

        elif event.unicode == '.' or event.unicode == ',':
            self.input += event.unicode

        self.box_color(paragraph)
