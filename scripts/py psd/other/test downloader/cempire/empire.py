

#https://cdn.smutstone.com/s2/comics/city/01/6_00.jpg

#3.6.53
#3.7.94

# Img
# https://www.cuntempire.com/assets/animations/characters/character1.png" # 1-36
# https://www.cuntempire.com/assets/animations/characters/character36.json

#?v=1607593192525

# XHR
#https://www.cuntempire.com/assets/sound/sounds.json?v=1607593192525
#https://www.cuntempire.com/assets/sound/sounds.mp3?v=1607593192525

import requests
import os
import zipfile

extensions = ["png", "json"]
characters_count = 36
character_address = "https://www.cuntempire.com/assets/animations/characters/character{number}.{extension}"

#address = character_address.format(number = 1, extension = "png")
#print(address)

def download_all():
    for e in extensions:
        for i in range(1, characters_count + 1):
            address = character_address.format(number = i, extension = e)
            content = download(address)
            
            splitted = address.split("/")
            directory = splitted[-2]
            filename = splitted[-1]
            path = os.path.join(directory, filename)

            if not os.path.exists(directory):
                os.mkdir(directory)
                print("directory created")

            save(content, path)

    print("all files downloaded")

def download(address):
    response = requests.get(address)
    return response.content

def save(content, path):
    with open(path, "wb") as f:
        f.write(content)

def get_files(directory):
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths 

def folder_to_zip():
    files = get_files("characters")

    with zipfile.ZipFile("characters.zip", "w") as f:
        for file in files:
            f.write(file)

    print("zip created")

#download_all()
#folder_to_zip()

print("done")
