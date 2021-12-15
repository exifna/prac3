import time
from math import ceil

from tools import Table, color
import inputimeout

table = Table()
table.print_table()

isWhite = True

start = time.time()

while True:
    locale = ''
    print(f'> Ход {f"{color.YELLOW}белых" if isWhite else f"{color.PURPLE}чёрных"}.{color.END}')
    try:
        locale = inputimeout.inputimeout(prompt=f'> Введите координаты до и после переноса в формате A1 B2: {color.GREEN}', timeout = 10)

    except KeyboardInterrupt:
        exit('\nGame close...')

    except:
        table.event_list.append(f'{"белые" if isWhite else "чёрные"} слишком долго думали...')


    if len(locale) >= 4:
        locale1 = locale[:2]
        locale2 = locale[-2:]
        check = table.check_move(locale1, locale2, isWhite)
        if check:
            table.move_by_letters(locale1, locale2)
    isWhite = not isWhite
    table.clear()
    table.print_table()
    if table.check_mat():
        exit(f'\n\nИгра завершена! Победила дружба ({table.who_win()}) за {f"{int((time.time() - start) // 60)} мин"}, {ceil((time.time() - start) - 60 * int((time.time() - start) // 60))} сек')



