from pyautogui import click, position, moveTo
from pynput.keyboard import Key, Listener
from os import system
from sys import platform
from time import sleep
from formatkit import text, background, formats, default

cls = lambda: system("cls") if platform in ["win32", "cygwin", "msys"] else system("clear")

class PyAutoClick:
    def __init__(self, position: tuple, clicks: int, delay: float, alert: bool = True) -> bool:
        """Initialization"""
        self.x = position[0]
        self.y = position[1]
        self.clicks = clicks
        self.delay = delay
        self.alert = alert
    def execute(self):
        """Executes an autoclicker with user-specified parameters"""
        moveTo(x=self.x, y=self.y)
        for _click in range(self.clicks):
            if (self.alert): print(background.yellow+formats.bold+f"Click number: {_click}"+default)
            click()
            sleep(self.delay)
            cls()
        return True


def on_press(key) -> None:
    if (str(key) == "'q'" or str(key) == "'w'"): cls()
    if (str(key) == "'q'"): quit()
    elif str(key) == "'w'":
        UserClicker = PyAutoClick(
            position=position(),
            clicks=int(input(
                background.green+formats.bold+"[?] Number of clicks:"+default+" ").replace("w", "")
                ),
            delay=float(
                input(background.green+formats.bold+"[?] Delay between clicks:"+default+" ").replace("w", "")
                )
        )
        UserClicker.execute()
        client()


def client(show_guide: bool = True, show_author: bool = True):
    cls()
    if show_guide:
        print(background.blue+formats.bold+"[I] To exit from clicker type 'q'")
        print("[I] To run the clicker type 'w'\n"+default)
        print(background.cyan+formats.bold+"[I] Important, point your course at the place where the program will click"+default)
        print(background.cyan+formats.bold+"[I] Also mportant, switch to english layout\n"+default)
    if show_author:
        print(f"🔮 {formats.italic}Author: Gleb Rodukov{default}")
        print(f"📂 {formats.italic}Github: https://github.com/rodukov/pyautoclick/{default}")
        print(f"🎆 {formats.italic}Included formatkit: https://github.com/rodukov/formatkit/\n{default}")
    with Listener(on_press=on_press) as listener: listener.join()

client()