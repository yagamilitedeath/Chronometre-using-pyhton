import time

from cs50 import get_string
while True:
    x=get_string("Enter the time en(D/H/M/S): ")
    if x == "D" or x == "d" or x == "h" or x == "H" or x == "M" or x == "m" or x == "S" or x == "s":
        break
    else:
        print("Please enter (D(days)/H(hours)/M(minutes)/S(seconds)")
timi=int(input(f"Enter the time in {x.upper()}: "))
if x=='d' or x=='D':
    timi=timi*60*60*24
    for k in range(timi, 0, -1):
        sec = k % 60
        minute = int(k / 60) % 60
        hour = int(k / 3600) % 24
        days = int(k / 86400)
        print(f"{days:02}:{hour:02}:{minute:02}:{sec:02}")
        time.sleep(1)
elif x=='H' or x=='h':
    timi=timi*60*60
    for k in range(timi, 0, -1):
        sec = k % 60
        minute = int(k / 60) % 60
        hour = int(k / 3600) % 24
        days = int(k / 86400)
        print(f"{days:02}:{hour:02}:{minute:02}:{sec:02}")
        time.sleep(1)
elif x=='m' or x=='M':
    timi=timi*60
    for k in range(timi, 0, -1):
        sec = k % 60
        minute = int(k / 60) % 60
        hour = int(k / 3600) % 24
        days = int(k / 86400)
        print(f"{days:02}:{hour:02}:{minute:02}:{sec:02}")
        time.sleep(1)
else:
    timi = timi
    for k in range(timi, 0, -1):
        sec = k % 60
        minute = int(k / 60) % 60
        hour = int(k / 3600) % 24
        days = int(k / 86400)
        print(f"{days:02}:{hour:02}:{minute:02}:{sec:02}")
        time.sleep(1)
