#INELEGANT Key Tracker
import string
import os
import pygame
import threading


DATA_HEAD = '''
------------------
 TOTAL KEYS TYPED
------------------
'''
TITLE = '\n{}:\n'
LABEL = '\n{key}: {count}'

# #add letter count
# DATA_TEMPLATE += TITLE.format('Letter')
# for letter in string.ascii_uppercase:
#     DATA_TEMPLATE += LABEL.format(name=letter)
# #add punctuation count
# for punctuation in '.!?\'\":;':
#     DATA_TEMPLATE += LABEL.format(name=punctuation)
# #add miscellaneous keys
# for i in ['SPACE', 'BACKSPACKE', 'ENTER']:
#     DATA_TEMPLATE += LABEL.format(name=i)

class KeyUpdater:

    def __init__(self):
        if os.path.isfile('program_data.txt'):
            with open('program_data.txt') as f:
                counts = f.readlines()
                self.key_counts = eval(counts[0].strip())
        else:
            self.key_counts = {i: 0 for i in string.ascii_lowercase}

    def update(self, event):
        if event:
            if event.unicode.lower() in string.ascii_lowercase:
                self.key_counts[event.unicode.lower()] += 1

    def save(self):
        #saves data for later use by program
        with open('program_data.txt', 'w') as f:
            f.write(str(self.key_counts))

        #saves data for user
        data = DATA_HEAD
        data += TITLE.format('Letters')
        for i, j in self.key_counts.items():
            data += LABEL.format(key=i, count=j)
        with open('key_counts.txt', 'w') as f:
            f.write(data)


def main():
    updater = KeyUpdater()
    update_thread = threading.Thread(target=updater.update(None))
    update_thread.start()
    pygame.init()
    screen = pygame.display.set_mode((100, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                updater.save()
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                updater.update(event)


if __name__ == '__main__':
    main()
