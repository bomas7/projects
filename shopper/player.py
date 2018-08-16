#player module

class Inventory:

    def __init__(*args):
        self.items = *args

class Player:

    def __init__(self, username):
        self.username = username
