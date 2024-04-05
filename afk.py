# You'll never be AFK with this script running in the background.

import time as t
import random as r
import pyautogui as pag
from notifypy import Notify


def mouse_bot(s):

    while True:
        x, y = r.randint(600, 700), r.randint(200, 600)
        pag.moveTo(x, y, s)
        t.sleep(1)


def notification():
    notify = Notify()
    notify.title = "AFK Bot Running"
    notify.message = "The AFK bot is currently running. You may leave for your business."
    notify.send()


if __name__ == "__main__":
    notification()
    menu = "M O U S E  B O T".center(30, ' ')

    try:
        speed = float(input(
            f"\n{menu}\n\n Enter the mouse speed : \n\n (0.0 => instantaneous movement 😮)\n (0.5 => a little  slower ... 😗)\n (1.0 => quiet slow to be honest 😐)\n\n Your choice >> "))
        print("\n You can go AFK now. 😁\n\n\n (Press Ctrl+C to stop the bot.)")
        mouse_bot(speed)

    except KeyboardInterrupt:
        print("\n\n The bot has been stopped! 😶\n")
