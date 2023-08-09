import pyautogui as pg
import pygetwindow as pw
import os
from dotenv import load_dotenv

def autoclick_reg(password):

    load_dotenv()

    reg = pw.getWindowsWithTitle(os.environ.get("KEY_NAME"))[0]

    pg.moveTo(1024, 610, 0.5)
    pg.click()
    reg.restore()
    reg.activate()
    pg.moveTo(reg.left+220, reg.top+175, 0.5)
    pg.click()
    pg.write(password)
    pg.moveTo(reg.left+220, reg.top+230, 0.5)
    pg.click()
