# Program to greet on the basis of time of day
import time as t

hour = int(t.strftime('%H'))

def greet(hour):
    if hour in range(0, 13):
        print("\n Good Morning, Sir!\n")
    elif hour in range(13, 19):
        print("\n Good Afternoon, Sir!\n")
    elif hour in range(19, 21):
        print("\n Good Evening, Sir!\n")
    elif hour in range(21, 0):
        print("\n Good Night, Sir!\n")

t.sleep(5)
greet(hour)