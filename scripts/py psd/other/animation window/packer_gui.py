# https://docs.python.org/3/glossary.html#term-eafp
# https://docs.python.org/3/glossary.html#term-annotation
# https://docs.python.org/3/glossary.html#term-type-hint

import os
import re
from typing import List

import tkinter as tk
from tkinter import ttk, filedialog

root = tk.Tk()
root.geometry("300x400")
root.title("Packer")

EXTENSION = ".png"

class FolderEntry:

    def __init__(self, path, root_path, files):
        self.path = path
        self.root_path = root_path.replace("\\", "/")
        self.files = files
        
        # https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
        folder_name = self.root_path.split("/")[-1]
        search_pattern = "\[(.+?)\]"
        found = re.search(search_pattern, folder_name)
        if found:
            value = found.group(1)
            x, y = value.split("x")
            self.grid_size = (int(x), int(y))

    def __str__(self) -> str:
        return f"{self.grid_size} {self.files}"

folder_entries = []

def populate_tree():
    pass

def handle_folder(r:str, folder:List[str]) -> List[str]:
    """
    files = []
    for file in folder:
        if EXTENSION in file and file.endswith(EXTENSION):
            file_path = os.path.join(r, file)
            files.append(file_path)
    """
    files = [file for file in folder if file.endswith(EXTENSION)]
    return files

def onClick_GetFolders():
    
    path = filedialog.askdirectory()

    if len(path) > 0:

        for r, d, f in os.walk(path):
            if len(f) > 0:
                files = handle_folder(r, f)
                folder_entry = FolderEntry(path, r, files)
                #print(len(f))
                #print(f)
                #print(folder_entry)
                folder_entries.append(folder_entry)
                #print("#")
            else:
                #print("!")
                pass

        for e in folder_entries:
            print(e)
            
    else:
        print("Path is empty")


btn_folders = ttk.Button(root, text = "Get Folders", command = onClick_GetFolders)
btn_folders.pack()

tree_view = ttk.Treeview(root)

scrollbar = ttk.Scrollbar(root, command = tree_view.yview)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

tree_view['columns'] = ("Grid", "Q", "W")
tree_view.configure(yscrollcommand = scrollbar.set)

w = 100

tree_view.column("#0", width = w, minwidth = w)
tree_view.column("Grid", anchor = tk.W, width = w, minwidth = w)
tree_view.column("Q", anchor = tk.W, width = w, minwidth = w)
tree_view.column("W", anchor = tk.W, width = w, minwidth = w)

tree_view.heading("#0", text = "Label", anchor = tk.W)
tree_view.heading("Grid", text = "grid", anchor = tk.W)
tree_view.heading("Q", text = "q", anchor = tk.W)
tree_view.heading("W", text = "w", anchor = tk.W)

data = [
    ("q", "1", "a"),
    ("w", "2", "b"),
    ("e", "3", "c"),
    ("r", "4", "d"),
    ("t", "5", "e"),
    ("y", "6", "f")
]

for i in range(20):
    index = i % len(data)
    row = data[index]
    tree_view.insert(parent = "", index = tk.END, iid = i, text = str(i), values = row)

#tree_view.insert(parent = "", index = tk.END, iid = 0, text = "Parent", values = ("Q", "w", "e"))
#tree_view.insert(parent = "", index = tk.END, iid = 1, text = "p1", values = ("W", "w", "e"))
#tree_view.insert(parent = "", index = tk.END, iid = 2, text = "p2", values = ("E", "w", "e"))

# same
#tree_view.insert(parent = "0", index = tk.END, iid = 3, text = "p2", values = ("R", "w", "e"))
#tree_view.move("3", "0", "0")

tree_view.pack(fill = tk.BOTH, expand = tk.TRUE, padx = 10, pady = 10)

root.mainloop()

print("Done")










