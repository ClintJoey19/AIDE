import pyautogui
import time

def automate(codes):
    time.sleep(5)

    # automated data entry
    for code in codes:
        pyautogui.typewrite(code, 0)
        pyautogui.press('enter')