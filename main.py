import random
import datetime
from click_timer import click_timer
from autoclick import autoclick_reg

password = input('Senha: ')

while True:
    now = datetime.datetime.now()
    autoclick_reg(password)
    t = random.randrange(1770, 1830)
    print(f'Próxima senha em {t//60:02d}:{t%60:02d}')
    click_timer(t)
    print(f'Ultima senha inserida às {now.strftime("%H:%M")}')
    