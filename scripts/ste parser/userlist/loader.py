from bs4 import BeautifulSoup           # pip install beautifulsoup4

with open('userlist.html') as f:
    contents = f.read()

#print (len(contents))

html = BeautifulSoup(contents, 'html.parser')

body = html.find('tbody')

ids = []

for entry in body:
    a = entry.find('a')
    href = a['href']
    name = a.text

    shit = 'index.php?inventorygame-appid-'
    gameId = href.replace(shit, '')

    i = gameId + "# " + name
    ids.append(i)

with open ('parsed_userlist.txt', 'w') as f:
    for id in ids:
        f.write(id + '\n')

#print (body)

"""
<tr class="odd" role="row"><td class="name sorting_1">
<a class="red" href="index.php?inventorygame-appid-410110">12 is Better Than 6</a>
</td><td>9</td><td>2</td><td>0x (2 of 5 Cards)</td></tr>
"""


