# импорт библиотеки представляющей перечисления
from enum import Enum


class TokenKind(Enum):
    # Класс-наследник перечисления
    var = 1
    num = 2
    op_br = 3
    cl_br = 4
    func = 5
    op = 6
