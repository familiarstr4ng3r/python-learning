import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('#15')
root.geometry('300x400')

def open():
    path = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Mondi', 
                                    filetypes = [('Images', '*.png *.jpg'), ('All files', '*.*')])

    if path:
        label['text'] = path
    else:
        label['text'] = 'smth'

btn = tk.Button(text = 'open', command = open)
btn.pack()

label = tk.Label()
label.pack()

root.mainloop()