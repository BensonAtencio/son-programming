import pyautogui as pg
import time

i = 0
# x = pg.position()
# print(x)

# pyautogui.click()

time.sleep(5)

while i < 5:
    pg.click()
    pg.write("Hello")
    pg.press('enter')
    # pg.click()
    i += 1
