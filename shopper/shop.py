#shop module

class Item:

    def __init__(self, name, use, description, cost):
        self.name = name
        self.use = use
        self.description = description
        self.cost = cost

    @classmethod
    def from_str(cls, str):
        name, use, description, cost = str.split(' - ')
        return cls(name, use, description, cost)


class Shop:

    def __init__(self):
        with open('stock.txt') as f:
            items = f.readlines()
        self.stock = [Item.from_str(i.strip()) for i in items]
