import pyautogui as pg
import pygetwindow as pw

reg_freq= pw.getWindowsWithTitle('Registro de Ponto v2.1')[0]
def autoclick_regfreq(password):
   
    pg.moveTo(1024, 610, 0.5)
    pg.click()
    reg_freq.activate()
    reg_freq.restore()
    pg.moveTo(reg_freq.top+215, reg_freq.left+155, 0.5)
    pg.click()
    pg.write(password)
    pg.moveTo(reg_freq.top+215, reg_freq.left+205, 0.5)
    pg.click()


# reg_freq.activate()
