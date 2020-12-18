import requests
import time
from tqdm import tqdm

#address = "https://loot.farm/fullpriceDOTA.json"
#address = "http://ipv4.download.thinkbroadband.com/20MB.zip" # doesnt work at all
#address = "https://fastest.fish/lib/downloads/100MB.bin"   # only via browser
address = "http://www.ovh.net/files/100Mb.dat"
#address = "https://www.steamcardexchange.net/index.php?inventorygame-appid-211820" # no content-length

filename = address.split('/')[-1]
chunk_size = 1024 * 1024
unit = 'MB'

start_time = time.time()
response = requests.get(address, stream = True)

#print(response.headers)
content_length_key = "Content-Length"


if content_length_key in response.headers:
    content_length = response.headers[content_length_key]
    print(content_length)
else:
    print("content_length is None")

def download():
    content_length = int(content_length)

    #std.py 158 line

    with open(filename, "wb") as f:
        downloader = tqdm(iterable = response.iter_content(chunk_size = chunk_size),
                          total = content_length / chunk_size, unit = unit)
        for data in downloader:
            f.write(data)

'''
def shit():
    d = 0
    if content_length:
        for chunk in response.iter_content(1024):
            d += len(chunk)
            percentage = d/int(content_length)
            sys.stdout.write(str(percentage))
'''

#print(len(response.content))
print("Done")
print(time.time() - start_time)
