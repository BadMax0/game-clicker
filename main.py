import sys
import time

from pynput import keyboard
from pynput.mouse import Button, Controller

is_click = False
DEFAULT_SLEEP_TIME = 1


def on_release(key):
    global is_click
    if key.char == "s":
        print("start clicking")
        is_click = True
    elif key.char == "e":
        print("end clicking")
        is_click = False


def main():
    listener = keyboard.Listener(
        # on_press=on_press,
        on_release=on_release
    )
    listener.start()

    try:
        sleep_time = float(sys.argv[1])
    except IndexError:
        sleep_time = DEFAULT_SLEEP_TIME
    mouse = Controller()
    while True:
        time.sleep(sleep_time)
        if is_click:
            mouse.click(Button.left)


if __name__ == "__main__":
    main()
