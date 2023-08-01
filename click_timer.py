import time

def click_timer(s):
    while s>=0:
        mins, secs = divmod(s, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        s -= 1