# Program to greet on the basis of time of day
import time as t

hour = int(t.strftime('%H'))

if hour in range(0,13):
  print("\n Good Morning, Sir!")
elif hour in range(13,19):
  print("\n Good Afternoon, Sir!")
elif hour in range(19,21):
  print("\n Good Evening, Sir!")
