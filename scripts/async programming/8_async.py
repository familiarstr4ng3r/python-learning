import requests
from time import time

def get_file(uri):
    r = requests.get(uri, allow_redirects = True)
    return r

def write_file(response):
    # https://loremflickr.com/cache/resized/65535_50138825602_aa1b28e2f6_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    filename = 'images/' + filename

    with open(filename, 'wb') as f:
        f.write(response.content)

def main():
    t0 = time()
    uri = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(uri))

    print(time() - t0)

#if __name__ == '__main__':
#    main()



########

import asyncio
import aiohttp
from time import time

def write_image(data):
    t = int(time() * 1000)
    filename = 'images/file-{}.jpg'.format(str(t))
    with open(filename, 'wb') as f:
        f.write(data)

async def fetch_content(uri, session):
    async with session.get(uri, allow_redirects = True) as response:
        data = await response.read()
        write_image(data)

async def main2():
    uri = 'https://loremflickr.com/320/240'
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(uri, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)




























