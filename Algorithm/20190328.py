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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    list=''

    for i in S:
        if i in prec:
            if i != '(' and opStack.size() != 0 and prec[opStack.peek()] >= prec[i]:
                list += opStack.pop()
            opStack.push(i)
        elif i ==')':
            while opStack.peek() != '(':
                list += opStack.pop()
            opStack.pop()
        else:
            list+=i

    while not opStack.isEmpty():
        list+=opStack.pop()

    return list

S="A-(B-C)*D"
print(solution(S))
