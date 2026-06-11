import curses
import time

def type_text(stdscr):
    stdscr.keypad(True)

    target = "Hello! I am Bay Max, your personal healthcare companion."
    typed = ""

    startTime = time.time()

    while True:
        correct = 0
        stdscr.clear()

        stdscr.addstr(0, 0, target, curses.color_pair(3))

        for i, ch in enumerate(typed):
            if i < len(target) and ch == target[i]:
                stdscr.addstr(0, i, ch, curses.color_pair(2))
                correct +=1 
            else:
                stdscr.addstr(0, i, ch, curses.color_pair(1))
            
        words = len(typed.split())
        elapsed = time.time() - startTime
        if elapsed > 0:
            stdscr.addstr(2, 0, f"WPM: {int((words / elapsed) * 60)}")

        stdscr.refresh()

        if len(typed) == len(target):
            break

        key = stdscr.getkey()

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            typed = typed[:-1]

        elif len(key) == 1:
            typed += key 
    
    stdscr.addstr(0,0, f"Accuracy: {correct/len(target) * 100}")
    stdscr.addstr(4, 0, "Done! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    curses.start_color() 
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    type_text(stdscr)    

curses.wrapper(main)