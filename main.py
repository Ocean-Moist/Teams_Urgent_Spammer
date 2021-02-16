import pyautogui
import time

message = input("type your message: ")
if message:
    time.sleep(5)
    x = 1
while x > 0:
    pyautogui.click(848, 1060)
    time.sleep(.1)
    pyautogui.click(835, 996)
    time.sleep(.1)
    pyautogui.click(1106, 1020)
    time.sleep(.1)
    pyautogui.write(message)
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    pyautogui.write('Sent using AnnoyBot 3000 (patent pending)')
    time.sleep(.1)
    pyautogui.press('enter')