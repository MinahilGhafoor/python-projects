import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Promodoro Timer")
root.geometry('500x300')
root.resizable(False, False)

bg_image = tk.PhotoImage(file="background.png")

# Create label with image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

promodoro_label = tk.Label(root, text="25 minutes 5 minutes",
                        font=("Palatino Linotype", 20, "bold"),
                        fg="white",bg="#2D3436",
                        relief="raised",
                        borderwidth=3)

promodoro_label.pack()

timer_label = tk.Label(root, text="25:00", font=("Arial", 30))
timer_label.pack()

break_timer_label = tk.Label(root, text="5:00", font=("Arial", 30))
break_timer_label.pack()


time_left = 25 * 60
break_time_left = 5 * 60

running = False
break_running = False

def timer():
    global time_left, running

    mins = time_left // 60
    secs = time_left % 60

    running = True

    timer_label.config(text=f"{mins:02d}:{secs:02d}")

    if time_left > 0:
        running = True
        time_left -= 1
        root.after(1000, timer)

    if time_left == 0:
        
        instantiate()

def instantiate():
    global break_time_left, running

    mins = break_time_left // 60
    secs = break_time_left % 60


    break_timer_label.config(text=f"{mins:02d}:{secs:02d}")

    if break_time_left > 0:

        break_time_left -= 1
        root.after(1000, instantiate)

    if break_time_left == 0:
        
        return messagebox.showinfo( "A pomodoro cycle has been completed successfully.")
        


    
def start():
    global running

    if not running:
        running = True
        timer()


start_timer = tk.Button(root,
                        text="Start Timer",
                        font=("Gabriola", 18, "bold"),
                        bg="#27AE60",fg="white",
                        relief="groove",
                        borderwidth=4,
                        cursor="hand2",
                        command=timer
)

start_timer.place(x=342, y=187)

root.mainloop()
