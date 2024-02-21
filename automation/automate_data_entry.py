import pyautogui
import time

def automate(codes):
    time.sleep(3)

    # process here not done


    # find the app icon
    img = "./assets/note.png"
    icon_loc = pyautogui.locateOnScreen(img)
    pyautogui.click(icon_loc, interval=2)

    # automated data entry
    for code in codes:
        pyautogui.typewrite(code, 0)
        pyautogui.press('enter')