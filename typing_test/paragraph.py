import random


class Paragraph:

    def __init__(self, cpl=40):
        #cpl = characters per line

        with open('paragraphs.txt') as f:
            self.paragraph = random.choice(f.readlines()).strip()

        words = self.paragraph.split(' ')
        self.lines = []
        adder = words[0]
        for i in words[1:]:
            if len(adder + i) + 1 <= cpl:
                adder += ' ' + i
            else:
                self.lines.append(adder)
                adder = i
        self.lines.append(adder)

        self.count = 0

        #cur = current
        self.cur_line = 0
        self.cur_words = self.lines[self.cur_line].split(' ')
        self.cur_word = self.cur_words[0]

    def status_update(self):
        self.count += len(self.cur_word) + 1
        if self.cur_words.index(self.cur_word) == len(self.cur_words) - 1:
            if self.cur_line + 1 == len(self.lines):
                self.cur_line += 1
                return
            self.cur_line += 1
            self.cur_words = self.lines[self.cur_line].split(' ')
            self.cur_word = self.cur_words[0]
        else:
            self.cur_word = self.cur_words[self.cur_words.index(self.cur_word) + 1]
