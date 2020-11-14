# https://younglinux.info/tkinter/menu.php
# https://www.youtube.com/watch?v=ZS2_v_zsPTg
# https://python-scripts.com/tkinter-introduction
import tkinter as tk

root = tk.Tk()
root.title('#46')
root.geometry('300x400+100+100')        # w h x y
root.minsize(300, 400)

def open():
    pass

def printText(text):
    print(text)

menuBar = tk.Menu(root)
root.config(menu = menuBar)

fileMenu = tk.Menu(menuBar, tearoff = False)
recentFilesMenu = tk.Menu(fileMenu, tearoff = False)
recentFilesMenu.add_command(label = "1", command = lambda: printText("1 text"))
recentFilesMenu.add_command(label = "2", command = lambda: printText("2 text"))
recentFilesMenu.add_command(label = "3", command = lambda: printText("3 text"))

fileMenu.add_command(label = "Open", command = open)
fileMenu.add_cascade(label = "Recent files", menu = recentFilesMenu)
fileMenu.add_command(label = "Exit", command = root.quit)

editMenu = tk.Menu(menuBar, tearoff = 0)
editMenu.add_command(label = "Undo", command = lambda: printText("Undo text"))
editMenu.add_command(label = "Redo", command = lambda: printText("Redo text"))
editMenu.add_separator()
editMenu.add_command(label = "Cut", command = lambda: printText("Cut text"))
editMenu.add_command(label = "Copy", command = lambda: printText("Copy text"))

menuBar.add_cascade(label = "File", menu = fileMenu)
menuBar.add_cascade(label = "Edit", menu = editMenu)

def showPopup(event):
    global x, y
    x = event.x
    y = event.y
    popupMenu.post(event.x_root, event.y_root)

def drawCircle():
    offset = 30
    canvas.create_oval(x, y, x + offset, y + offset,
                       fill = "white", outline = "red")

def drawSquare():
    offset = 30
    index = canvas.create_rectangle(x, y, x + offset, y + offset)
    print(index)

def clearCanvas():
    canvas.delete(tk.ALL)

canvas = tk.Canvas(width = 200, height = 200, bg = "grey")
canvas.pack(fill = tk.BOTH, expand = tk.TRUE)
canvas.bind("<Button-3>", showPopup)

popupMenu = tk.Menu(tearoff = False)
popupMenu.add_command(label = "Circle", command = drawCircle)
popupMenu.add_command(label = "Square", command = drawSquare)
popupMenu.add_command(label = "Triangle...")
popupMenu.add_separator()
popupMenu.add_command(label = "Clear", command = clearCanvas)

root.mainloop()
