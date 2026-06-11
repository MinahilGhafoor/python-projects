def clock():
    while True:
        
        now = datetime.now()
        print(f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}",end="\r")

clock()