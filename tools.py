import os
import traceback
from typing import List

class Table:                # поле
    def __init__(self):
        from figurs import Peshka, Horse, Ladya, Elephant, Qeen, King
        self.table : List[List[Figura]]= [
            [x(0) for x in [Ladya, Horse, Elephant, Qeen, King, Elephant, Horse, Ladya]],
            [Peshka(0) for x in range(8)],

        ]
        self.table.extend([[None for ii in range(8)] for x in range(4)])
        self.table.extend(
            [[Peshka(1) for x in range(8)],
            [x(1) for x in [Ladya, Horse, Elephant, Qeen, King, Elephant, Horse, Ladya]]]
        )
        self.event_list = list()
        self.letters = {'A' :0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}

    def print_table(self):
        tmp = 8
        if len(self.event_list) > 8:
            self.event_list = self.event_list[-8:]
        print(color.GREEN + '┏' + '━' * 16 + '┳━┓' + color.END)
        for i in self.table:
            print(f'{color.GREEN}┃{color.END}', end='')
            for ii in i:
                if ii:
                    print(f'{ii.symbol} ', end = '')
                else:
                    print('  ', end = '')
            print(f'{color.GREEN}┃{color.END}{color.CYAN}{color.BOLD}{tmp}{color.END}{color.GREEN}┃{color.END} {self.event_list[8 - tmp] if len(self.event_list) - (8 - tmp) > 0 else ""}')
            tmp -= 1

        print(color.GREEN + '┣━' + '━' * 15 + '┛ ┃' + color.END)
        print(color.GREEN +  '┃' + ''.join([f'{color.CYAN}{color.BOLD}{x}{color.END} ' for x in list(self.letters.keys())]) + color.GREEN + '  ┃' + color.END)
        print(color.GREEN +   '┗━━' +'━' * 16+ '┛' + color.END)

    def check_move(self, first_place, second_place, isWhite : bool) -> bool:
        try:

            x1 = self.letters[first_place[0]]
            y1 = 8 - int(first_place[1])
            x2 = self.letters[second_place[0]]
            y2 = 8 - int(second_place[1])

            figura = self.table[y1][x1]
            x = x2 - x1
            y = -(y2 - y1)

            # if not x + y:
            #     return False

            if not x and not y:
                return False

            if self.table[y1][x1].isWhite != isWhite:
                    return False

            if self.table[y2][x2]:
                if self.table[y2][x2].isWhite == isWhite:
                    return False

            if figura.figura_type == Figura_types.peshka:   # проверка: если 1й ход - то только 2 прямо если 2е - то только 1 вперед если есть кто-то, то
                if isWhite:
                    y = -(y2 - y1)
                else:
                    y = (y2 - y1)
                if y < 0:
                    return False
                if not figura.steps and x == 0 and y <= 2 and y > 0 and not self.table[y2][x2]:
                    return True
                if x == 0 and y == 1 and not self.table[y2][x2]:
                    return True
                if abs(x) == 1 and y == 1 and self.table[y2][x2]:
                    return True

            elif figura.figura_type == Figura_types.ladya:
                if x:
                    s = list(sorted([x1, x2]))
                    return True not in [self.table[y2][i] != None for i in range(s[0] + 1, s[1])]

                if y > 0:
                    s = list(sorted([y1, y2]))
                    return True not in [self.table[i][x2] != None for i in range(s[0], s[1])]

                if y < 0:
                    s = list(sorted([y1 + 1, y2 + 1]))
                    return True not in [self.table[i][x2] != None for i in range(s[0], s[1])]

                if self.table[y2][x2]:
                    return self.table[y2][x2].isWhite != isWhite
                return True

            elif figura.figura_type == Figura_types.horse:
                if abs(x) + abs(y) != 3:
                    return False
                return self.table[y2][x2].isWhite != isWhite if self.table[y2][x2] else True

            elif figura.figura_type == Figura_types.elephant:
                if abs(x) != abs(y) :
                    return False

                if self.table[y2][x2]:
                    if self.table[y2][x2].isWhite == isWhite:
                        return False
                if x>0 and y > 0:    # +
                    return True not in [self.table[y1 - i][x1 + i] != None for i in range(1, abs(x))]

                if x < 0 and y > 0:  # +
                    return True not in [self.table[y1 -  i][x1 - i ] != None for i in range(1, abs(x))]

                if x > 0 and y < 0:  # +
                    return True not in [self.table[y1 + i][x1 + i] != None for i in range(1, abs(x))]

                if x < 0 and y < 0:
                    return True not in [self.table[y1 + i][x1 - i] != None for i in range(1, abs(x))]

                if not self.table[y2][x2]:
                    return True

            elif figura.figura_type == Figura_types.qeen:

                if abs(x) != abs(y) and x * y != 0:
                    return False

                if x * y == 0:
                    if x:
                        s = list(sorted([x1, x2]))
                        return True not in [self.table[y2][i] != None for i in range(s[0] + 1, s[1])]

                    if y > 0:
                        s = list(sorted([y1, y2]))
                        return True not in [self.table[i][x2] != None for i in range(s[0], s[1])]

                    if y < 0:
                        s = list(sorted([y1 + 1, y2 + 1]))
                        return True not in [self.table[i][x2] != None for i in range(s[0], s[1])]

                if x>0 and y > 0:    # +
                    return True not in [self.table[y1 - i][x1 + i] != None for i in range(1, abs(x))]

                if x < 0 and y > 0:  # +
                    return True not in [self.table[y1 -  i][x1 - i ] != None for i in range(1, abs(x))]

                if x > 0 and y < 0:  # +
                    return True not in [self.table[y1 + i][x1 + i] != None for i in range(1, abs(x))]

                if x < 0 and y < 0:
                    return True not in [self.table[y1 + i][x1 - i] != None for i in range(1, abs(x))]

                if not self.table[y2][x2]:
                    return True

            elif figura.figura_type == Figura_types.king:

                return not bool(x*y > 1)

            '''
C2 -> C4
D7 -> D5
D1 -> B3
D8 -> D6
B3 -> B6
D6 -> B6
E1 -> D1
E8 -> D7


            '''
            return False

        except:
            return False

    def check_mat(self):
        kings = 0
        for i in self.table:
            for ii in i:
                if ii:
                    if ii.figura_type == Figura_types.king:
                        kings += 1
        return kings != 2

    def who_win(self):
        black = False
        white = False
        for i in self.table:
            for ii in i:
                if ii:
                    if ii.figura_type == Figura_types.king:
                        if ii.isWhite:
                            white = True
                        else:
                            black = True
        if not black:
            return 'чёрные'

        if not white:
            return 'белые'

    def move_by_letters(self, first_place : str, second_place : str):
        try:
            x1 = self.letters[first_place[0]] + 1
            y1 = int(first_place[1])
            x2 = self.letters[second_place[0]] + 1
            y2 = int(second_place[1])
            self.event_list.append(f'{("белые" if self.table[8- y1][x1 -1].isWhite else "чёрные") if self.table[8- y1][x1 -1] else "ничего"}: {first_place} -> {second_place}')
            self.move_figure(x1, y1, x2, y2)
        except:
            pass

    def move_figure(self, x1 : int, y1 : int, x2 : int, y2 : int):
        try:
            self.table[8- y1][x1 -1].steps += 1
            if self.table[8 - y2][x2 - 1]:
                self.event_list.append(f'{color.UNDERLINE}{color.BOLD}{"БЕЛЫЕ" if self.table[8- y1][x1 -1].isWhite else "ЧЁРНЫЕ"} съедают.{color.END}')
            self.table[8 - y2][x2 - 1] = self.table[8- y1][x1 -1]
            self.table[8 -y1][x1 - 1] = None
        except:
            pass

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class Figura:               # общий класс фигур
    def __init__(self, isWhite : int, symbol : str, figura_type : str):
        self.isWhite = isWhite
        self.symbol = symbol
        self.figura_type : int = figura_type
        self.steps = 0



class Figura_types:
    peshka = 0
    horse  = 1
    ladya  = 2
    elephant = 3
    qeen   = 4
    king   = 5

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

