from time import sleep
from tools import Table, color

table = Table()
table.print_table()

isWhite = True

while True:
    print(f'> Ход {f"{color.YELLOW}белых" if isWhite else f"{color.PURPLE}чёрных"}.{color.END}')
    locale = input(f'> Введите координаты до и после переноса в формате A1 B2: {color.GREEN}')
    if len(locale) >= 4:
        locale1 = locale[:2]
        locale2 = locale[-2:]
        check = table.check_move(locale1, locale2, isWhite)
        if check:
            table.move_by_letters(locale1, locale2)
            isWhite = not isWhite
    table.clear()
    table.print_table()


