import threading
import time

stop = False

def stopwatch():
    start_time = time.time()

    while not stop:

        elapsed = time.time() - start_time

        h = int(elapsed // 3600)
        m = int((elapsed % 3600) // 60)
        s = int(elapsed % 60)
        cs = int((elapsed % 1) * 100)
        print(f"{h:02d}:{m:02d}:{s:02d}:{cs:02d}", end="\r")
        time.sleep(0.01)

def wait_for_stop():
    global stop
    input()
    stop = True

t = threading.Thread(target=wait_for_stop)
t.start()

stopwatch()