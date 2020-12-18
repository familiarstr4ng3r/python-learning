from PIL import ImageTk, Image
import numpy as np

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

init_dir = r'C:\Users\User\Desktop\2D RUNNER\CONTENT\KEYFRAMES'
#init_dir = os.getcwd()

root = tk.Tk()

windowSize = (400, 500)

screenSize = (root.winfo_screenwidth(), root.winfo_screenheight())
windowCenter = (int(screenSize[0] / 2 - windowSize[0] / 2), 
                int(screenSize[1] / 2 - windowSize[1] / 2))


root.title("Cucumber")
root.geometry(f'{windowSize[0]}x{windowSize[1]}+{windowCenter[0]}+{windowCenter[1]}')
root.minsize(windowSize[0], windowSize[1])
root.attributes("-topmost", True)
root["bg"] = "light gray"

scaleFactor = 0.3
images = []

def get_files():
    filetypes = [('Images', '*.png *.jpg'), ('All files', '*.*')]
    files = filedialog.askopenfilenames(initialdir = init_dir, filetypes = filetypes)
    return files
                        

def onClick_Open():
    files = get_files()
    
    slider_var.set(0)
    global images
    images.clear()
    
    for f in files:
        add_image(f)

    update_slider(len(files))


def onClick_LoadGrid():
    files = get_files()

    slider_var.set(0)
    global images
    images.clear()

    for f in files:
        slice_image(f)

    update_slider(len(images))


def slider_action(value):
    value = slider_var.get()
    
    global images
    image = images[value]
    label.config(image = image)

def update_slider(length):
    if length > 0:
        slider_length = length - 1
        slider.config(state = tk.NORMAL, to = slider_length)

        image = images[0]
        label.config(image = image)
    else:
        #label.config(image = None)
        slider.config(state = tk.DISABLED)
    

def add_image(path):
    image = Image.open(path)
    image = resize_image(image, scaleFactor) # should i resize here ?
    image = ImageTk.PhotoImage(image)
    
    global images
    images.append(image)

def slice_image(path):
    image = Image.open(path)
    image = resize_image(image, scaleFactor) # better way resize here (only at once)

    rows = entries[0].get()
    if len(rows) > 0: rows = int(rows)
    
    columns = entries[1].get()
    if len(columns) > 0: columns = int(columns)

    (frame_w, frame_h) = (image.width // rows, image.height // columns)

    for y in range(columns):
        for x in range(rows):
            arr = np.array(image)
            arr = arr[y * frame_h:y * frame_h + frame_h, x * frame_w:x * frame_w + frame_w]
            add_array_image(arr)
    
    
def add_array_image(array):
    image = Image.fromarray(array)
    #image = resize_image(image, scaleFactor) # should i resize here ?
    image = ImageTk.PhotoImage(image)
    
    global images
    images.append(image)

#def onClick_Debug():
#    size = (frame.winfo_width(), frame.winfo_height())
#    print(size)

def resize_image(image, scale):
    (w, h) = (image.width * scale, image.height * scale)
    (w, h) = (int(w), int(h))
    image = image.resize((w, h))
    return image

open_button = ttk.Button(root, text = "Open Frames", command = onClick_Open)
open_button.pack(fill = tk.X)

grid_button = ttk.Button(root, text = "Open Grid", command = onClick_LoadGrid)
grid_button.pack(fill = tk.X)

#command = lambda: action(flag)

entries = []

for i in range(2):
    e = tk.Entry(root)
    e.pack()
    entries.append(e)

slider_var = tk.IntVar()
slider = tk.Scale(root, from_ = 0, to = 5, orient = tk.HORIZONTAL,
                    variable = slider_var, command = slider_action, state = tk.DISABLED)
slider.pack(fill = tk.X, padx = 50)

frame = ttk.LabelFrame(root, text = "Image")
frame.pack()

label = tk.Label(frame)
label.pack()

root.mainloop()

#print('done')











