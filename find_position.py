import pyautogui as pg
import pygetwindow as pw
import time

reg_freq= pw.getWindowsWithTitle('Registro de Ponto v2.1')[0]

print(290-reg_freq.top, 305-reg_freq.left)

pg.moveTo(290, 305,0.5)

reg_freq.activate()
time.sleep(2)
reg_freq.maximize()
time.sleep(2)
# reg_freq.minimize()
# time.sleep(2)
reg_freq.restore()
time.sleep(2)
reg_freq.close()




# while True:
#     x, y = pg.position()
#     time.sleep(0.05)
#     print(f'x: {str(x)}, y: {str(y)}', end="\r")

    

    