import tkinter as tk
from tkinter import messagebox
import pyscreenshot as ImageGrab        # creating image 
import pytesseract                      # text recognition
import pyperclip                        # copying text to clipboard
#import cv2
#import numpy as np
#from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

alpha = 0.2
width = 1000
height = 600
offset = 10

clickedX = 0
clickedY = 0

screenX = 0
screenY = 0

endX = 0
endY = 0

def motionAction(event):
    dashes = (2, 2)
    canvas.delete('lines')
    canvas.create_line(event.x, 0, event.x, 1000, dash = dashes, tags = 'lines')
    canvas.create_line(0, event.y, 1000, event.y, dash = dashes, tags = 'lines')

def onPress(e):
    global clickedX, clickedY
    clickedX = e.x
    clickedY = e.y

    global screenX, screenY
    screenX = root.winfo_pointerx()
    screenY = root.winfo_pointery()

    #print(f"press {e}")

def onRelease(e):
    canvas.delete('rect')

    global endX, endY
    endX = root.winfo_pointerx()
    endY = root.winfo_pointery()

    ## TODO: make screenshot
    makeImage()

    #print(f"release {e}")

def onDrag(e):
    canvas.delete('rect')
    canvas.create_rectangle(clickedX, clickedY, e.x, e.y, tags = 'rect', width = 2)

    #print("b1 drag")

def makeImage():
    box = (screenX, screenY, endX, endY)
    image = ImageGrab.grab(box)

    #fileName = "image1.png"

    #image.save(fileName)

    #screen = np.array(box)
    #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    #cv2.imwrite(fileName, screen)
    #image = cv2.imread(fileName)

    #image = Image.open(fileName)

    # eng, rus
    text = pytesseract.image_to_string(image, lang='ukr')
    text = text.strip()

    if (len(text) > 0):
        messagebox.showinfo(title = 'Converted text', message = text)
        pyperclip.copy(text)

root = tk.Tk()
root.title('Simple OCR by Mondi')
root.wm_attributes('-alpha', alpha)
#root.wm_attributes("-topmost", True)
root.geometry(f'{width}x{height}')
#root.resizable(width = False, height = False)

canvas = tk.Canvas(root, width = width - offset, height = height - offset, bg = "gray")
#canvas.pack()
canvas.place(relwidth = 1, relheight = 1)

canvas.bind('<Motion>', motionAction)
root.bind('<ButtonPress-1>', onPress)
root.bind('<ButtonRelease-1>', onRelease)
root.bind('<B1-Motion>', onDrag)

root.mainloop()

#print('app closed')
