import requests
from bs4 import BeautifulSoup as bs

from parsing import Parser

# TODO:
# parse id from separate file
# create parser object and put id
#! start parsing games in loop with delay
#! async download

def onDownload(percentage):
    print(percentage)

#ids = readGames('games.txt')
#print(ids)

p = Parser('games.txt')
p.parse(onDownload=onDownload)
p.getInfo()

quit(0)


# !


response = requests.get('https://www.steamcardexchange.net/index.php?inventorygame-appid-211820')
html = bs(response.content, 'html.parser')

#container = html.select('.inventory-game-card-container')
items = html.find_all('div', class_ = 'inventory-game-card-item')

# for i, item in enumerate(items):
#     print(i)
#     print(item)
#     print("###")

print(len(items))

for item in items:
    nameContainer = item.find('div', class_ = 'name-image-container')
    #print(nameContainer)
    cardName = nameContainer.find('span', class_ = "card-name gray")

    if cardName:
        name = cardName.text
    else:
        continue

    priceContainer = item.find('div', class_ = "price-container").find_all('span')

    # stock = priceContainer.find_all('span')
    #print(stock)
    
    #for s in stock:
    #    print(s.text)
    
    stockAmount = priceContainer[0].text
    worth = priceContainer[1].text
    price = priceContainer[2].text
    
    print(name + stockAmount + worth + price)

input("Press something")