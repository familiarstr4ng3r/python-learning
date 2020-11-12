#https://younglinux.info/tkinter/menu.php
#https://www.youtube.com/watch?v=Grbx15jRjQA

import grequests
import threading

#from tkinter import *
import tkinter as tk
from tkinter import ttk

from parsing import Parser

root = tk.Tk()
root.title('Simple App')
root.geometry('500x500')

fillbar = ttk.Progressbar(root, orient = tk.HORIZONTAL, length = 100, mode = 'determinate')
fillbar.pack()

fillbar2 = ttk.Progressbar(root)
fillbar2.pack()

p = Parser('games.txt')

def asyncParse():
    
    baseUri = 'https://www.steamcardexchange.net/index.php?inventorygame-appid-'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
    requests = []
    for i in range(10):
        uri = f"{baseUri}570"
        #uri = "https://www.google.com"
        requests.append(grequests.get(uri, headers = headers))
    print ('1')
    grequests.map(requests)
    print ('2')

    for r in requests:
        print(r.response.status_code)

def parse():
    btnParse['state'] = tk.DISABLED
    #root.update_idletasks()
    t = threading.Thread(target=threadParse())
    t.start()
    
def threadParse():
    p.parse(onDownload = onDownload)
    result = p.getInfo()

    for r in result:
        text = result[r]
        #textbox.insert(tk.END, text)
        print (text)

    btnParse['state'] = tk.NORMAL

def onDownload(percentage01):
    fillbar['value'] = percentage01 * 100
    root.update_idletasks()
    #if percentage01 == 1:
    #    btnParse['state'] = tk.NORMAL

def onClear():
    fillbar['value'] = 0

btnParse = ttk.Button(root, text = "Parse")
btnParse.config(command = parse)
btnParse.pack()

btnClear = ttk.Button(root, text = "Clear")
btnClear.config(command = onClear)
btnClear.pack()

textbox = tk.Text(root, width = 50, height = 20)# font = ('Consolas', 14)
textbox.pack()

#textbox.configure(state = tk.DISABLED)
#textbox['state'] = tk.DISABLED

root.mainloop()