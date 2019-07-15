'''
 스택의 응용 수식의 후위 표기법
 중위표기법 => (A+B) * (C+D) 연산자가 피연산자들 사이에 위치
 후위표기법 => AB+CD+* 연산자가 피연사자들 뒤에 위치
 중위 표현식 => 후위 표현식
 만약 연산자를 만나면 스택에 집어넣음
 스택이 비어있지 않다면 스택 안의 연산자와 비교해서 우선순위가 더 높으면 Push,
 낮으면 스택안의 원소를 pop하고 자신은 push한다.
 만약 연산자의 우선순위가 동일하면 스택안에 있는 것을 먼저 pop하고 자신은 push한다.
 여는 괄호를 만나면 스택에 push, 닫는 괄호를 만나면 여는 괄호가 나올 때까지 pop

'''

class ArrayStack:
    def __init__(self):
        self.data=[]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

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



