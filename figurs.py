from tools import Figura, Figura_types


class Peshka(Figura):   # пешка
    def __init__(self, isWhite : int):
        symbol = '♟' if isWhite else '♙'

        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.peshka)

class Horse(Figura):     # конь
    def __init__(self, isWhite : int):
        symbol = '♞' if isWhite else '♘'

        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.horse)

class Ladya(Figura):     # ладья
    def __init__(self, isWhite : int):
        symbol = '♜' if isWhite else '♖'

        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.ladya)


class Elephant(Figura):     # слон
    def __init__(self, isWhite : int):
        symbol = '♝' if isWhite else '♗'

        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.elephant)


class Qeen(Figura):     # королева
    def __init__(self, isWhite : int):
        symbol = '♛' if isWhite else '♕'

        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.qeen)

class King(Figura):     # король
    def __init__(self, isWhite : int):
        symbol = '♚' if isWhite else '♔'
        super().__init__(isWhite = isWhite, symbol = symbol, figura_type=Figura_types.king)
