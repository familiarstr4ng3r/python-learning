#https://docs.google.com/spreadsheets/u/1/d/1hjjCzyHYzaIeasTX7IpjOoQsB4UQdTjxxFmEjfaL8vU/
#export?format=zip&id=1hjjCzyHYzaIeasTX7IpjOoQsB4UQdTjxxFmEjfaL8vU

#https://docs.google.com/spreadsheets/export?format=zip&id=
#1hjjCzyHYzaIeasTX7IpjOoQsB4UQdTjxxFmEjfaL8vU

# https://webformatter.com/html

import requests
import zipfile
import io
from bs4 import BeautifulSoup

SHEET_LINK = "https://docs.google.com/spreadsheets/export?format=zip&id="
ID = "1liqJ34DsWhKAnYmGVYkRkbHYMZ_W8LOP_4p7QWm5-1s"
test_id = "12sfqBl8Q6ci6IsY0Lu4hcikJ4H4VSRKl_HMbhsdwQkk"

def download(uri):
    response = requests.get(uri)

    zip_bytes = io.BytesIO(response.content)
    zip_file = zipfile.ZipFile(zip_bytes, "r")

    #print (zip_file.namelist())
    name = zip_file.namelist()[0]

    with zip_file.open(name) as f:
        html_text = f.read()

    return html_text

def parse(html_text):

    data = []
    
    html = BeautifulSoup(html_text, "html.parser")
    grid_container = html.find("div", class_ = "ritz grid-container")
    body = grid_container.find("tbody")

    for item in body:
        entries = item.find_all("td")
        row = []
        for e in entries:
            row.append(e.text)
        data.append(row)
        #print(row)

    return data

def save():
    with open("result.txt", "w", encoding = "utf-8") as f:
        #f.writelines(data)
        for line in csv:
            f.write("%s\n" % line)

uri = SHEET_LINK + ID
html_text = download(uri)

data = parse(html_text)

separator = ";"
csv = [separator.join(row) for row in data]
print(csv)

save()

print("done")

