import tkinter as tk
from Json.jsonFunctions import *
import Save_Entry.saveEntry as s 

PATH = s.JSON_PATH

def start_root():

    root = tk.Tk()
    root.configure(bg="white")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x, y = (screen_width - 400) // 2, (screen_height - 200) // 2

    root.geometry(f"400x200+{x}+{y}")

    root.resizable(False, False)

    return root


def show_checkboxes(root):
    data = loadJson(PATH)

    selected_vars = []

    for entry in data:
        name = entry['Username']
        site = entry['Site']

        var = tk.IntVar()

        tk.Checkbutton(root, text=f"Username : {name} | Site : {site}", variable=var).pack(anchor="w")
        selected_vars.append((var, entry))

    return selected_vars

def delEntry():
    root = start_root()
    selected_vars = show_checkboxes(root)
    tk.Button(root, text="Submit", command=quit).pack(pady=10)
    data = loadJson(PATH)
    selected = [entry for var, entry in selected_vars if var.get() == 1]
    for i in selected:
        data.remove(i)
    writeJson(PATH, data)

    
    root.mainloop()

    



