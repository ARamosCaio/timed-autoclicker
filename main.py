import random
import datetime
from click_timer import click_timer
from autoclick import autoclick_regfreq

password = input('Senha: ')

while True:
    t = random.randrange(10, 15)
    print(f'Próxima senha em {t//60:02d}:{t%60:02d}')
    click_timer(t)
    autoclick_regfreq(password)
    now = datetime.datetime.now()
    print(f'Ultima senha inserida às {now.strftime("%H:%M")}')
    