import os
import math
import time
import glob

import tkinter as tk
from tkinter import filedialog

from PIL import Image
import numpy as np
import cv2


def get_images(folder):
    images = []

    for root, dirs, files in os.walk(folder):

        for file in files:
            path = os.path.join(root, file)
            image = Image.open(path)
            images.append(image)

    return images


def get_horizontal_stack(images):
    grid_x, grid_y = (len(images), 1)

    image = images[0]
    w, h = image.size

    total_width = w * grid_x
    total_height = h * grid_y
    size = (total_width, total_height)
    
    background = Image.new("RGBA", size, 0)

    for i, image in enumerate(images):
        x = i * w
        background.paste(image, (x, 0))

    return background


def get_horizontal_padded(images, divisibility = None):
    grid_x, grid_y = (len(images), 1)

    image = images[0]
    w, h = image.size

    if not divisibility is None:
        frame_w = divisibility * math.ceil(w / divisibility)
        frame_h = divisibility * math.ceil(h / divisibility)
    else:
        frame_w = w
        frame_h = h

    total_width = frame_w * grid_x
    total_height = frame_h * grid_y
    size = (total_width, total_height)

    background = Image.new("RGBA", size, 0)

    x_diff = (frame_w - w) // 2
    y_diff = (frame_h - h) // 2

    for i, image in enumerate(images):
        x = i * frame_w + x_diff
        y = 0 + y_diff
        background.paste(image, (x, y))

    return background


def pack_grid(images, grid_x, grid_y, divisibility = None):
    w, h = images[0].size

    if not divisibility is None:
        frame_w = divisibility * math.ceil(w / divisibility)
        frame_h = divisibility * math.ceil(h / divisibility)
    else:
        frame_w = w
        frame_h = h
    
    total_width = frame_w * grid_x
    total_height = frame_h * grid_y
    size = (total_width, total_height)
    
    background = Image.new("RGBA", size, 0)

    x_diff = (frame_w - w) // 2
    y_diff = (frame_h - h) // 2

    for y in range(grid_y):
        for x in range(grid_x):
            x_pos = x * frame_w + x_diff
            y_pos = y * frame_h + y_diff

            index = y * grid_x + x
            if index >= len(images): continue

            image = images[index]
            background.paste(image, (x_pos, y_pos))

    return background


def show(image, scaleFactor = 0.5):
    image = np.array(image)
    h, w, _ = image.shape
    h = int(h * scaleFactor)
    w = int(w * scaleFactor)
    
    image = cv2.resize(image, (w, h))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save(image):
    filename = "result.png"
    image.save(filename)


def main_packer():
    t1 = time.time()
    
    image_folder = "images"
    images = get_images(image_folder)

    divisibility = 500
    
    #image = get_horizontal_stack(images)
    #image = get_horizontal_padded(images, divisibility)

    #for i in range(10):
    image = pack_grid(images, 2, 2, divisibility)

    print("Packed:", time.time() - t1)
    
    #save(image)
    print("Saved:", time.time() - t1)

    show_result = True
    if show_result: show(image)


def main_folders():
    root = tk.Tk()
    
    path = filedialog.askdirectory()

    if len(path) > 0:
        """
        ALL = "**/**"
        PNG = "**/*.png"
        
        for filename in glob.iglob(path + PNG, recursive = True):
            print(filename)
        """
        for r, d, f in os.walk(path):
            print(d)
            
            for file in f:
                if '.png' in file:
                    p = os.path.join(r, file)
                    print(p)

            print("#")
            
    else:
        print("Path is empty")

    # https://www.delftstack.com/ru/howto/python-tkinter/how-to-close-a-tkinter-window-with-a-button/
    root.destroy()


def main():
    main_packer()
    #main_folders()


if __name__ == "__main__":
    main()
    print("Done")










