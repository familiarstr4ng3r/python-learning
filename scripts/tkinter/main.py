# https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
#! 1-4
#? 5-7 calculator

import tkinter as tk

root = tk.Tk()
root.title('Mondi')
root.iconbitmap('icon.ico') # relative path, can be absolute too

#myLabel = tk.Label(root, text = 'Hello World!')
#myLabel.pack()

"""
labels = []
for i in range(3):
    label = tk.Label(root, text = f'Label: {i}')
    labels.append(label)

for i, label in enumerate(labels):
    label.grid(row = i, column = 0)
"""

def onClick(index):
    print(index)

def printText():
    text = e.get()
    buttons[0]['text'] = text
    #e.insert(len(text), "Mia")

buttons = []
for i in range(3):
    # command = lambda: onClick(index) #! bullshit

    button = tk.Button(root, text = f'Button: {i}', command = printText, padx = 50, pady = 20)
    buttons.append(button)

for i, button in enumerate(buttons):
    #button.grid(row = 0, column = i)
    button.pack()

e = tk.Entry(root, width = 20, borderwidth = 5)
e.pack()

root.mainloop()