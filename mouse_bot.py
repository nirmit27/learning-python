# You'll never be AFK with this script running in the background ...

import time as t
import random as r
import pyautogui as pag


def mouse_bot(s):

    while True:

        # Co-ordinates within which the mouse moves on the screen ...
        x, y = r.randint(600, 700), r.randint(200, 600)

        # Invoking the module's function ...
        pag.moveTo(x, y, s)

        # Interval between successive mouse events ...
        t.sleep(2)


# Driver code
if __name__ == "__main__":

    menu = "M O U S E  B O T".center(30, ' ')

    try:
        speed = float(input(
            f"\n{menu}\n\n Enter the mouse speed : \n\n (0.0 => instantaneous movement 😮)\n (0.5 => a little  slower ... 😗) \n (1.0 => quiet slow to be honest 😐)\n\n Your choice >> "))
        print("\n You can go AFK now. 😁\n\n\n (Press Ctrl+C to stop the bot.)")
        mouse_bot(speed)
#
    except KeyboardInterrupt:
        print("\n\n The bot has been stopped! 😶")
