#Day 26: Solution of Exercise 2

import time

timestamp = time.strftime('%H:%M:%S')
print("Current Time is:", timestamp)

hour = int(time.strftime('%H'))

if (hour >= 0 and hour < 12):
    print("Good Morning Sir!")
elif (hour >= 12 and hour < 17):
    print("Good Afternoon Sir!")
elif (hour >= 17 and hour < 21):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
