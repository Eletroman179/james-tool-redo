import pyautogui
import time
import os

cd = os.getcwd() #

pyautogui.press("win")
pyautogui.typewrite("cmd")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.press("F11")
pyautogui.typewrite(f"cd {cd}")
pyautogui.press("enter")
pyautogui.typewrite("python main.py")
pyautogui.press("enter")
