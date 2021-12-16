# импорт пользовательских библиотек
from code.my_sympy.token import Token
from code.my_sympy.token_kind import TokenKind
from code.my_sympy.ops import Ops


class MySympy:
    # Sympy - библиотека для математических вычислений.
    # Она умеет работать со строковыми символами и выражениями.
    # Данный класс назван в ее честь в связи с тем, что тоже так умеет.
    delimiters = " ()+/*-^%"
    delimiters_set = set(delimiters)

    def __init__(self):
        """
        Инициализация и создание полей экземпляра класса.
        """
        self.variables = dict()
        self.tokens = []
        self.postfix_tokens = []
        self.prior = dict()
        self.ops = dict()
        self.create_prior()
        self.create_ops()

    def read_expression_from_str(self, input_str, quantity_variables):
        """
        Функция принимает выражение, представленное строкой,а также переменные в виде:
        'название_переменной=значение_переменной'.
        Здесь применяются различные проверки входных данных на предмет корректности.
        :param input_str: list
        :param quantity_variables: int
        :return: str ИЛИ None
        """
        # Если количество реально заданных переменных не соответствует предполагаемому числу, то это ошибка
        if len(input_str) - 1 != quantity_variables:
            return None
        expression = input_str[0][:]
        for i in range(1, quantity_variables + 1):
            temp = input_str[i][:]
            pos = temp.find('=')
            if pos > 0:
                name = temp[:pos]
                try:
                    value = float(temp[pos + 1:])  # если значение переменной не приводится к числовому типу, это ошибка
                    self.variables[name] = value
                except:
                    return None
        if len(self.variables) != quantity_variables:
            # если в итоге количество переменных не совпало с заявленным числом, это ошибка
            return None
        return expression

    def is_delimiter(self, symbol) -> bool:
        """
        Функция проверяет, является ли символ знаокм-разделителем, указанным в атребуте класса
        :param symbol: str
        :return: bool
        """
        return symbol in self.delimiters_set

    def create_tokens_from_expression(self, expression):
        """
        Функция создания токенов из выражения, представленного строкой.
        :param expression: str
        :return: bool ИЛИ None
        """
        # Заполняем спосик токенами
        ex = expression + " "
        i = 0
        while i < len(ex) - 1:
            name = ''
            if self.is_delimiter(ex[i]):
                if ex[i] == ' ':
                    i += 1
                    continue
                name = ex[i]
                i += 1
            else:
                while not self.is_delimiter(ex[i]):
                    name += ex[i]
                    i += 1
            self.tokens.append(Token(name, TokenKind.var))

        # Уточняем категории токенов
        for i in range(len(self.tokens)):
            if self.tokens[i].name[0] == '(':
                self.tokens[i].type = TokenKind.op_br
                continue
            if self.tokens[i].name[0] == ')':
                self.tokens[i].type = TokenKind.cl_br
                continue
            if self.tokens[i].name[0].isdigit():
                self.tokens[i].type = TokenKind.num
                continue
            if self.tokens[i].name[0].isalpha():
                if i < len(self.tokens) - 1 and self.tokens[i + 1].name[0] == '(':
                    self.tokens[i].type = TokenKind.func
                continue
            self.tokens[i].type = TokenKind.op

        # Проверяем выходные параметры
        for i, item in enumerate(self.tokens, start=0):
            if item.name == "-" and (i == 0 or self.tokens[i - 1].type == TokenKind.op_br):
                item.name = "opposite"
        return self.check_tokens() and self.check_variables()

    def check_tokens(self):
        """
        Функция проверки токенов на соответствие допустимым категориям.
        :return: bool
        """
        for item in self.tokens:
            if item.type == TokenKind.func:
                if item.name not in self.ops.keys():
                    return False
        return True

    def check_variables(self):
        """
        Функия проверки переменных
        :return: bool
        """
        for item in self.tokens:
            if item.type == TokenKind.var:
                if item.name not in self.variables.keys():
                    return False
        return True

    def create_prior(self):
        """
        Функция задает приоритеты операций
        :return: None
        """
        self.prior["+"] = 10
        self.prior["-"] = 10
        self.prior["*"] = 20
        self.prior["/"] = 20
        self.prior["^"] = 30
        self.prior["opposite"] = 10
        self.prior["%"] = 20

    def create_postfix_from_tokens(self):
        """
        Функция получения инфиксной формы заиси выражения (обратная польская нотация)
        :return: None
        """
        token_stack = []
        for item in self.tokens:
            if item.type == TokenKind.num or item.type == TokenKind.var:
                self.postfix_tokens.append(item)
            elif item.type == TokenKind.op_br:
                token_stack.insert(0, item)
            elif item.type == TokenKind.cl_br:
                while token_stack[0].type != TokenKind.op_br:
                    self.postfix_tokens.append(token_stack[0])
                    token_stack.pop(0)
                token_stack.pop(0)
            elif item.type == TokenKind.op:
                if len(token_stack) != 0:
                    while len(token_stack) != 0 and \
                            ((token_stack[0].type == TokenKind.op and
                              self.prior[item.name] <= self.prior[token_stack[0].name])
                             or token_stack[0].type == TokenKind.func):
                        self.postfix_tokens.append(token_stack[0])
                        token_stack.pop(0)
                token_stack.insert(0, item)
            elif item.type == TokenKind.func:
                while len(token_stack) and token_stack[0].type == TokenKind.func:
                    self.postfix_tokens.append(token_stack[0])
                    token_stack.pop(0)
                token_stack.insert(0, item)

        while len(token_stack) != 0:
            self.postfix_tokens.append(token_stack[0])
            token_stack.pop(0)

    def create_ops(self):
        """
        Функция, инициализирующая словарь функций операций.
        :return: None
        """
        self.ops["+"] = Ops.op_plus
        self.ops["-"] = Ops.op_minus
        self.ops["*"] = Ops.op_mul
        self.ops["/"] = Ops.op_div
        self.ops["^"] = Ops.op_deg
        self.ops["opposite"] = Ops.op_opposite
        self.ops["%"] = Ops.op_odiv
        self.ops["sin"] = Ops.op_sin
        self.ops["cos"] = Ops.op_cos
        self.ops["tan"] = Ops.op_tan
        self.ops["acos"] = Ops.op_acos
        self.ops["asin"] = Ops.op_asin
        self.ops["atan"] = Ops.op_atan

    def result_expression(self):
        """
        Функция подсчета значения выражения с учетом подготовительных манипуляций.
        :return: float
        """
        s = []
        for item in self.postfix_tokens:
            if item.type == TokenKind.num:
                try:
                    s.insert(0, float(item.name))
                except:
                    return None
            elif item.type == TokenKind.var:
                for key, value in self.variables.items():
                    if key == item.name:
                        s.insert(0, value)
            elif item.type == TokenKind.func or item.type == TokenKind.op:
                for key, value in self.ops.items():
                    if key == item.name:
                        s.insert(0, value(s))
        return s[0]

    def calculate(self, input_str, quantity_variables):
        """
        Функция, считающая значение выражения, заданного строкой и содержащего переменные, заданные строкой.
        :param input_str: list
        :param quantity_variables: int
        :return: float ИЛИ None
        """
        try:
            expression = self.read_expression_from_str(input_str, quantity_variables)
            if expression is not None:
                if self.create_tokens_from_expression(expression):
                    self.create_postfix_from_tokens()
                    return self.result_expression()
        except:
            pass
        return None
