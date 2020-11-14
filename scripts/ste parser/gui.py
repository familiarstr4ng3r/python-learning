from threading import Thread
from datetime import datetime
from winsound import Beep

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import font

from parsing import Parser

root = tk.Tk()

parseContinuously = False

windowTitle = 'Application'       # config
windowSize = (300, 400)     # config

screenSize = (root.winfo_screenwidth(), root.winfo_screenheight())
windowCenter = (int(screenSize[0] / 2 - windowSize[0] / 2), 
                int(screenSize[1] / 2 - windowSize[1] / 2))

root.title(windowTitle)
root.iconbitmap('Resources/favicon_blue.ico')
root.geometry(f'{windowSize[0]}x{windowSize[1]}+{windowCenter[0]}+{windowCenter[1]}')
root.minsize(windowSize[0], windowSize[1])

parser = Parser('userlist.txt')

def insertLine(text):
    text += '\n'
    textbox.insert(tk.END, text)

def changeButtonState(isParsing):
    btnParse['state'] = tk.DISABLED if isParsing else tk.NORMAL
    btnClear['state'] = tk.NORMAL if isParsing else tk.DISABLED

def parse():
    root.focus()

    changeButtonState(True)

    global parseContinuously
    parseContinuously = True

    thread = Thread(target=threadParse)
    thread.start()
    
def threadParse():

    onDownload(0)
    parser.parse(onDownload = onDownload)
    parser.getInfo()

    now = datetime.now()
    timeText = now.strftime('%H:%M:%S')
    
    insertLine(timeText)
    
    length = len(parser.tradableGames)

    if length > 0:
        insertLine(str(length))
        insertLine(str(parser.tradableGames))
        Beep(500, 1000)
    else:
        #textbox.insert(tk.END, str(parser.responseCodes) + '\n')
        pass

    textbox.yview(tk.END)

    if parseContinuously:
        threadParse()
    else:
        changeButtonState(False)
        root.title(windowTitle)

def onDownload(percentage01):
    percent = percentage01 * 100
    fillbar['value'] = percent
    root.title(f'[{round(percent)}%] {windowTitle}')

def onClear():
    root.focus()

    global parseContinuously
    parseContinuously = False
    btnClear['state'] = tk.DISABLED

frame = ttk.Frame(root)
frame.pack(fill = tk.X, padx = 10, pady = 10)

fillbar = ttk.Progressbar(frame)
fillbar.pack(fill = tk.X, expand = tk.TRUE)

btnParse = ttk.Button(frame, text = "Parse")
btnParse.config(command = parse)
btnParse.pack(side = tk.LEFT, fill = tk.X, expand = tk.TRUE, padx = 0, pady = 0, ipadx = 0, ipady = 0)

btnClear = ttk.Button(frame, text = "Stop")
btnClear.config(command = onClear, state = tk.DISABLED)
btnClear.pack(side = tk.LEFT, fill = tk.X, expand = tk.TRUE, padx = 0, pady = 0, ipadx = 0, ipady = 0)

"""
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

textbox = tk.Text(root, width = 50, height = 10)
textbox.pack()

textbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = textbox.yview)
"""

textFont = ('Tahoma', 12)

textbox = ScrolledText(root, width = 30, height = 10, font = textFont)
textbox.pack(fill = tk.BOTH, expand = tk.TRUE)
#textbox.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

for i, id in enumerate(parser.ids):
    text = f"{i+1}: {id}"
    insertLine(text)

"""
fontLabel = tk.Label(root, text = "label")
fontLabel.pack(pady = 20)

fonts = list(font.families())

for i, f in enumerate(fonts):
    text = f'{i}: {f}'
    insertLine(text)

i = 0

def pressUp(key):
    global i
    i -= 1
    updateFont()

def pressDown(key):
    global i
    i += 1
    updateFont()

def updateFont():
    global i, textFont

    fontName = fonts[i]
    fontLabel['text'] = fontName

    textFontList = list(textFont)
    textFontList[0] = fontName
    textFont = tuple(textFontList)

    textbox['font'] = textFont

root.bind("<Up>", pressUp)
root.bind("<Down>", pressDown)
"""

root.mainloop()