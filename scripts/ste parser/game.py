class Game:

    name = 'game'
    cards = []
    tradableCards = []

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def update(self):
        #print("*")
        #print (self.cards)
        
        #! way 1: clear then iterate and append
        #self.tradableCards.clear()

        #for c in self.cards:
        #    if c.isTradable():
        #        self.tradableCards.append(c)

        #! way 2: 'where' linq query like c# 
        self.tradableCards = [c for c in self.cards if c.isTradable()]

        #? question: why first way is bullshit without clearing list

        #print (self.tradableCards)

    def isValid(self):
        length = len(self.tradableCards)
        #print (self.name + ": " + str(length))
        return length > 0

    def __repr__(self):
        return f'{self.name} : {self.tradableCards.__repr__()}'
