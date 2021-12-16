class Token:
    # Класс, представляющий собой объект Токен. Используется для
    # преобразования выражения с использованием обратной польской нотации (инфиксной записи)
    def __init__(self, name='no_name', type_='no_type'):
        """
        Конструктор для объекта типа Токен.
        :param name: str
        :param type_: TokenType
        """
        self.name = name
        self.type = type_
