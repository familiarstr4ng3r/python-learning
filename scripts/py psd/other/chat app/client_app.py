import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

windowSize = (500, 400)

screenSize = (root.winfo_screenwidth(), root.winfo_screenheight())
windowCenter = (int(screenSize[0] / 2 - windowSize[0] / 2), 
                int(screenSize[1] / 2 - windowSize[1] / 2))

root.title('Cucumber')
root.geometry(f'{windowSize[0]}x{windowSize[1]}+{windowCenter[0]}+{windowCenter[1]}')
#root.minsize(windowSize[0], windowSize[1])

height_percentage = 0.8


topFrame = ttk.LabelFrame(text = 'All Messages')
topFrame.place(relwidth = 1, relheight = height_percentage)

padding = 10

textbox = ScrolledText(topFrame)
textbox.pack(fill = tk.BOTH, expand = tk.TRUE)
#textbox.place(relwidth = 1, relheight = height_percentage)

def onClick_Send():
    text = inputBox.get('1.0', 'end-1c')
    insertLine(text)
    inputBox.delete('1.0', tk.END)

def modified(shit):
    inputBox.edit_modified(False)
    text = inputBox.get('1.0', 'end-1c')
    sendButton['state'] = tk.NORMAL if len(text) > 0 else tk.DISABLED
    

frame = ttk.LabelFrame(text = 'Write Message')
frame.place(relwidth = 1, relheight = 1 - height_percentage, rely = height_percentage)

width_percentage = 0.8
inputBox = ScrolledText(frame)
inputBox.bind('<<Modified>>', modified)
#inputBox.place(relwidth = width_percentage, relheight = 1)

sendButton = ttk.Button(frame, text = 'Send message')
sendButton.config(command = onClick_Send)
#sendButton.place(relwidth = 1 - width_percentage, relheight = 1, relx = width_percentage)

##userFrame = ttk.LabelFrame(frame, text = 'Nickname')
##userFrame.place(height = 20, width = 20)
##userFrame.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)

sendButton.pack(side = tk.RIGHT, fill = tk.BOTH, expand = tk.TRUE)
inputBox.pack(side = tk.RIGHT, fill = tk.BOTH, expand = tk.TRUE)

def insertLine(text):
    text += '\n'
    textbox.insert(tk.END, text)
    textbox.yview(tk.END)

with open('lorem.txt') as f:
    insertLine(f.read())

root.mainloop()





















