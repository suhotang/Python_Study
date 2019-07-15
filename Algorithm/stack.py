class ArrayStack:
    def __init__(self):
        self.data=[]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size==0

    def push(self,item):
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

# 수식 s가 인자로 주어질 때, 이 수식을 후위 표기법을 따르는 수식으로 변환하여 반환
def solution(S):
    opStack = ArrayStack()
    answer = ""

    for c in S:
        if c in prec:
            if c is not '(' and not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                answer += opStack.pop()
            opStack.push(c)

        elif c is ')':
            while not opStack.isEmpty():
                op = opStack.pop()
                if op is not '(':
                    answer += op

        else:
            answer += c

    while not opStack.isEmpty():
        op = opStack.pop()
        if op is not '(':
            answer += op

    return answer

s="A+B+C"
print(solution(s))