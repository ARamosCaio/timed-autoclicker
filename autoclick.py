import pyautogui as pg
import pygetwindow as pw
import os
from dotenv import load_dotenv

load_dotenv()



def autoclick_reg(password):
    reg = pw.getWindowsWithTitle(os.environ['KEY_NAME'])[0]
    reg.restore()
    reg.activate()
    pg.moveTo(1024, 610, 0.5)
    pg.click()
    pg.moveTo(reg.left+220, reg.top+125, 0.5)
    pg.click()
    pg.write(password)
    pg.moveTo(reg.left+220, reg.top+125, 0.5)
    pg.click()

