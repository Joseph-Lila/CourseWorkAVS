# список для хранения точек графика
_points_store_ = [[], []]


def change_store(x, y):
    """
    Функция для смены значений хранимых точек, представляющих график функции.
    :param x: list
    :param y: list
    :return: None
    """
    global _points_store_
    _points_store_ = [x, y]


def points_store():
    """
    Геттер. Возвращает значение приватной переменной _points_store_.
    :return: list
    """
    global _points_store_
    return _points_store_
