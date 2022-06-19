from pyautogui import click, position, moveTo
from pynput.keyboard import Key, Listener
from os import system
from sys import platform
from time import sleep
from formatkit import text, background, formats, default

cls = lambda: system("cls") if platform in ["win32", "cygwin", "msys"] else system("clear")

class PyAutoClick:
    def __init__(self, position: tuple, clicks: int, delay: float) -> None:
        """Initialization"""
        self.x = position[0]
        self.y = position[1]
        self.clicks = clicks
        self.delay = delay
    def execute(self):
        """"""
        moveTo(x=self.x, y=self.y)
        for _click in range(self.clicks):
            print(f"Click number: {_click}")
            click()
            sleep(self.delay)
            cls()


def on_press(key) -> None:
    if str(key) == "'q'":
        cls()
        quit()
    elif str(key) == "'w'":
        cls()
        UserClicker = PyAutoClick(position=position(), clicks=int(input(background.green+formats.bold+"[?] Number of clicks:"+default+" ").replace("w", "")), delay=float(input(background.green+formats.bold+"[?] Delay between clicks:"+default+" ").replace("w", "")))
        UserClicker.execute()


def client():
    cls()
    print(background.blue+formats.bold+"[I] To exit from clicker type 'q'")
    print("[I] To run the licker type 'w'"+default)
    with Listener(on_press=on_press) as listener: listener.join()

client()