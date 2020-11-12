from game import Game
from card import Card

import requests                         # pip install requests
from bs4 import BeautifulSoup           # pip install beautifulsoup4
import datetime                         # default library

class Parser:

    ids = []
    baseUri = 'https://www.steamcardexchange.net/index.php?inventorygame-appid-'
    games = []
    tradableGames = []

    def __init__(self, ids):
        self.ids = ids

    def __init__(self, fileName):
        self.ids = self.readGames(fileName)

    def getInfo(self):

        self.tradableGames.clear()

        for g in self.games:
            g.update()
            if g.isValid():
                self.tradableGames.append(g)

        l = len(self.tradableGames)
        #print("len is " + str(l))
        #for g in self.tradableGames:
        #    print(g)
        
        now = datetime.datetime.now()
        timeText = now.strftime('%H:%M:%S')
        msg = f'Found {l} tradable games'

        result = {}
        result['time'] = timeText
        result['count'] = msg
        result['games'] = []

        for g in self.tradableGames:
            cardNames = [card.name for card in g.tradableCards]
            #infoText = g.name + ": " + cardNames.__str__()
            infoText = f'{g.name}: {cardNames}' # {g.cards} 
            #print(infoText)
            result['games'].append(infoText)

        return result

    def parse(self, onDownload = None):

        self.games.clear()

        for i, id in enumerate(self.ids):
            g = self.parseGame(self.baseUri + id)
            self.games.append(g)

            if onDownload:
                percentage01 = (i+1)/len(self.ids)
                onDownload(percentage01)
                #print (percentage01)

        #print ("Parsed all games")

    def readGames(self, fileName):
        arr = []
        with open(fileName) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('#'):
                    continue
                else:
                    index = line.find('#')
                    line = line[0:index]
                    line = line.strip()
                    arr.append(line)
        return arr
            
    def parseGame(self, uri):
        response = requests.get(uri)
        html = BeautifulSoup(response.content, 'html.parser')
        gameName = self.getGameName(html)
        gameCards = self.getGameCards(html)
        g = Game(gameName, gameCards)
        return g

    def getGameName(self, html):
        name = html.find('span', class_ = 'game-title').text
        return name

    def getGameCards(self, html):
        cards = []
        items = html.find_all('div', class_ = 'inventory-game-card-item')

        for entry in items:
            nameContainer = entry.find('div', class_ = 'name-image-container')
            cardName = nameContainer.find('span', class_ = "card-name gray")

            if not cardName:
                continue
            
            name = cardName.text

            priceContainer = entry.find('div', class_ = "price-container").find_all('span')

            info = []
            for i in range(3):
                info.append(priceContainer[i].text)
            
            c = Card(name, info)
            cards.append(c)

        return cards
