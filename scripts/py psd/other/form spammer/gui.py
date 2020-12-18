import json
import tkinter as tk
from tkinter import ttk

class GUI:
    
    def __init__(self, root, dictionary):
        self.root = root
        self.dictionary = dictionary
        self.var = tk.IntVar()

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill = tk.BOTH, expand = tk.TRUE, padx = 10, pady = 10)
        
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        self.create_entries()

    def pack(self):
        self.label = tk.Label(self.root, text = "146")
        self.label.pack()

        btn1 = ttk.Radiobutton(self.root, text = "Option 1", variable = self.var, value = 1, command = self.clicked)
        btn2 = ttk.Radiobutton(self.root, text = "Option 2", variable = self.var, value = 2, command = self.clicked)

        btn1.pack(anchor = tk.W)
        btn2.pack(anchor = tk.W)
        
    def clicked(self):
        value = self.var.get()
        self.label["text"] = value

    def create_entries(self):
        entry_dict = self.dictionary["entries"]

        for key in entry_dict:
            #entry_dict = self.dictionary[key]
            
            entry_label = ttk.Label(self.frame, text = key)
            entry_label.pack()

            #title_label = ttk.Label(self.frame, text = entry_dict[]["title"], wraplength = 500)#, justify = tk.LEFT)
            #title_label.pack(anchor = tk.W)

            label = tk.Message(self.root, text = entry_dict[key]["title"], justify = tk.LEFT)
            label.pack()
            
            self.create_entry(entry_dict[key])

    def create_entry(self, entry_dict):
        mode = entry_dict["mode"]

        if mode == "RadioButton":
            for a in entry_dict["answers"]:
                radioButton = ttk.Radiobutton(self.frame, text = a)
                radioButton.pack(anchor = tk.W)
        elif mode == "Checkbox":
            for a in entry_dict["answers"]:
                checkbox = ttk.Checkbutton(self.frame, text = a)
                checkbox.pack(anchor = tk.W)

with open("result_nupp_full.json") as f:
    dictionary = json.load(f)

#print(type(dictionary))

root = tk.Tk()
root.geometry("600x400")
root["bg"] = "gray"

gui = GUI(root, dictionary)
#gui.pack()

# command = lambda:clicked(r.get()

'''
checkVar = tk.IntVar()
check1 = ttk.Checkbutton(root, text = "c 1", variable = checkVar)
check2 = ttk.Checkbutton(root, text = "c 2", variable = checkVar)
check3 = ttk.Checkbutton(root, text = "c 3", variable = checkVar)

check1.pack()
check2.pack()
check3.pack()
'''



root.mainloop()
