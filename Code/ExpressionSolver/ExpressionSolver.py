from Code.ExpressionSolver.Token import Token
from Code.ExpressionSolver.TokenType import TokenType
from Code.ExpressionSolver.Operations import Operations


class ExpressionSolver:
    delimiters = " ()+/*-^%"
    delimiters_set = set(delimiters)

    def __init__(self):
        self.variables = dict()
        self.tokens = []
        self.postfix_tokens = []
        self.prior = dict()
        self.ops = dict()
        self.create_prior()
        self.create_ops()

    def read_expression_from_str(self, input_str, quantity_variables):
        expression = input_str[0][:]
        for i in range(1, quantity_variables + 1):
            temp = input_str[i][:]
            pos = temp.find('=')
            if pos > 0:
                name = temp[:pos]
                try:
                    value = float(temp[pos + 1:])
                    self.variables[name] = value
                except:
                    return None
        return expression

    def is_delimiter(self, symbol) -> bool:
        return symbol in self.delimiters_set

    def create_tokens_from_expression(self, expression):
        ex = expression + " "
        for item in ex:
            name = ''
            if self.is_delimiter(item):
                if item == ' ':
                    continue
                name = item
            else:
                while not self.is_delimiter(item):
                    name += item
                self.tokens.append(Token(name, TokenType.var))

        for i, item in enumerate(self.tokens, start=0):
            if item.name[0] == '(':
                item.type = TokenType.op_br
                continue
            if item.name[0] == ')':
                item.type = TokenType.cl_br
                continue
            if item.name[0].isdigit():
                item.type = TokenType.num
                continue
            if item.name[0].isalpha():
                if i < len(item) - 1 and self.tokens[i + 1].name[0] == '(':
                    item.type = TokenType.func
                continue
            item.type = TokenType.op

        for i, item in enumerate(self.tokens, start=0):
            if item.name == "-" and (i == 0 or self.tokens[i - 1].type == TokenType.op_br):
                item.name = "opposite"

    def create_prior(self):
        self.prior["+"] = 10
        self.prior["-"] = 10
        self.prior["*"] = 20
        self.prior["/"] = 20
        self.prior["^"] = 30
        self.prior["opposite"] = 10
        self.prior["%"] = 20

    def create_postfix_from_tokens(self):
        token_stack = []
        for item in self.tokens:
            if item.type == TokenType.num or item.type == TokenType.var:
                self.postfix_tokens.append(item)
            elif item.type == TokenType.op_br:
                token_stack.insert(0, item)
            elif item.type == TokenType.cl_br:
                while token_stack[0] != TokenType.op_br:
                    self.postfix_tokens.append(token_stack[0])
                    token_stack.pop()
                token_stack.pop()
            elif item.type == TokenType.op:
                if len(token_stack) != 0:
                    while len(token_stack) != 0 and \
                            ((token_stack[-1] == TokenType.op and
                              self.prior[item.name] <= self.prior[token_stack[0].name])
                             or token_stack[0].type == TokenType.func):
                        self.postfix_tokens.append(token_stack[0])
                        token_stack.pop()
                token_stack.insert(0, item)
            elif item.type == TokenType.func:
                while len(token_stack) and token_stack[0].type == TokenType.func:
                    self.postfix_tokens.append(token_stack[0])
                    token_stack.pop()
                token_stack.insert(0, item)
        while len(token_stack) != 0:
            self.postfix_tokens.append(token_stack[0])
            token_stack.pop()

    def create_ops(self):
        self.ops["+"] = Operations.op_plus
        self.ops["-"] = Operations.op_minus
        self.ops["*"] = Operations.op_mul
        self.ops["/"] = Operations.op_div
        self.ops["^"] = Operations.op_deg
        self.ops["opposite"] = Operations.op_opposite
        self.ops["%"] = Operations.op_odiv
        self.ops["sin"] = Operations.op_sin
        self.ops["cos"] = Operations.op_cos
        self.ops["tan"] = Operations.op_tan
        self.ops["acos"] = Operations.op_acos
        self.ops["asin"] = Operations.op_asin
        self.ops["atan"] = Operations.op_atan

    def result_expression(self):
        s = []
        for item in self.postfix_tokens:
            if item.type == TokenType.num:
                try:
                    s.insert(0, float(item))
                except:
                    return None
            elif item.type == TokenType.var:
                for key, value in self.variables:
                    if key == item.name:
                        s.insert(0, value)
            elif item.type == TokenType.func or item.type == TokenType.op:
                for key, value in self.ops:
                    if key == item.name:
                        s.insert(0, value(s))
        return s[0]

    def calculate(self, input_str, quantity_variables):
        expression = self.read_expression_from_str(input_str, quantity_variables)
        if expression is not None:
            self.create_tokens_from_expression(expression)
            self.create_postfix_from_tokens()
            return self.result_expression()
