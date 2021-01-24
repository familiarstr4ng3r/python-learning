from PIL import Image
import numpy as np
import cv2

import os

def resize(image, size):
  image = np.array(image)
  image = cv2.resize(image, size)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  return image

# def resize(image, w, h):
#   return resize(image, (w, h))

def resizeImages(images, w, h):
  arr = []
  for image in images:
    newImage = resize(image, (w, h))
    arr.append(newImage)
  return arr

def getImagesAtPath(path):
  paths = []
  with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            paths.append(entry.path)
  return paths

def getImages(paths):
  images = []
  for path in paths:
    image = Image.open(path)
    images.append(image)
  return images

def main():
  savePath = "C:/Users/User/Desktop/python image resizer/images hd"
  paths = getImagesAtPath("D:/runner store design/screens")
  images = getImages(paths)
  images = resizeImages(images, 1280, 720)
  for i, p in enumerate(paths):
    name = p.split("\\")[-1]
    name = savePath + "/" + name
    cv2.imwrite(name, images[i])
  
if __name__ == "__main__":
  main()