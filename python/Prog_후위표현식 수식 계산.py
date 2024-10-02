class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    stack = []
    ret = []
    
    for token in tokenList :
        if isinstance(token, int) :
            ret.append(token)
        elif token == '(' :
            stack.append(token)
        elif token == ')' :
            while stack[-1] != '(' :
                ret.append(stack.pop())
            stack.pop()
        else :
            while stack and prec[stack[-1]] >= prec[token] :
                ret.append(stack.pop())
            stack.append(token)
    
    while stack :
        ret.append(stack.pop())
            

    return ret


def postfixEval(tokenList):
    stack = []
    for token in tokenList :
        if token == '+' :
            stack.append(stack.pop() + stack.pop())
        elif token == '-' :
            stack.append(stack.pop(-2) - stack.pop())
        elif token == '*' :
            stack.append(stack.pop() * stack.pop())
        elif token == '/' :
            stack.append(stack.pop(-2) / stack.pop())
        else :
            stack.append(token)
    return stack[-1]


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val