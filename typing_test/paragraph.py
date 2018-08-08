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
