import time

def countdown_timer(seconds):
    
    while seconds > 0:

        h = seconds // 3600
        m = (seconds % 3600 ) // 60
        s = seconds % 60

        print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("00:00:00 - Done!")

def main():
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    secs = (hours * 3600) + (minutes * 60) + seconds

    countdown_timer(secs)

if __name__ == "__main__":
    main()