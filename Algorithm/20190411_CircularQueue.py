class CircularQueue:
    # 전달 인자 n은 max길이
    def __init__(self, n):
        self.maxCount=n
        self.data = [None] * n  # None을 각 위치에 넣음
        self.count=0  # 현재 들어있는 원소 개수
        self.front=-1
        self.rear=-1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count==self.maxCount

    # 큐에 데이터 원소 추가
    def enqueue(self,x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear= (self.rear+1)%self.maxCount
        self.data[self.rear]=x
        self.count+=1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue Empty')
        self.front = (self.front)%self.maxCount
        x= self.data[self.front]
        self.count-=1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[self.front]

    def solution(x):
        return 0

