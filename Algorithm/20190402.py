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

    opStack = ArrayStack()
    postfixList = []
    #중위로 표현된 리스트를 후위로 바꿈

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()

        else:
            # 일반 연산자일 때 (+,*,/,-)
            if token != '(' and opStack.size() != 0 and prec[opStack.peek()] > prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int :
            valStack.push(token)

        elif token == '*':
            n1=valStack.pop()
            n2=valStack.pop()
            result=n2*n1
            valStack.push(result)

        elif token == '/':
            n1=valStack.pop()
            n2=valStack.pop()
            result=n2/n1
            valStack.push(result)

        elif token == '+':
            n1=valStack.pop()
            n2=valStack.pop()
            result=n2+n1
            valStack.push(result)

        elif token == '-':
            n1=valStack.pop()
            n2=valStack.pop()
            result=n2-n1
            valStack.push(result)

    return valStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    print(tokens)
    postfix = infixToPostfix(tokens)
    print(postfix)
    val = postfixEval(postfix)
    return val

expr="(1+2)*(3+4)"
print(solution(expr))
