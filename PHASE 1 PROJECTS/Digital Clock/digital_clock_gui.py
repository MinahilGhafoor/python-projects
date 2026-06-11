
from datetime import datetime
from tkinter import *

root = Tk()
root.geometry("220x170")
root.title("DIGITAL CLOCK")
root.configure(bg="black")
root.resizable(False, False)


text = Label(root, bg="black", fg="white", )
text.config(font =("Courier", 37))

button = Button(root, text="Stop", width=25, command=root.destroy)

def update_clock():
    now = datetime.now()
    text.config(text=f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")
    root.after(1000, update_clock) 

text.pack()
button.pack()

update_clock()
root.mainloop()
