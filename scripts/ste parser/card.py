class Card:

    name = ''
    info = []

    count = 0

    def __init__(self, name, info):
        self.name = name
        self.info = info

    #def __str__(self):
    #    return f'{self.name} = {self.info}'

    def __repr__(self):
        return f'{self.name} = {self.count}'# = {self.info[0]}

    def isTradable(self):
        stock = self.info[0]
        stock = stock[7:8]
        self.count = int(stock)
        return self.count > 1
