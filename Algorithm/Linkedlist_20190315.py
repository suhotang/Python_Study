class Node:
    # 노드 초기화
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # 파이썬 내장 함수 repr()
    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
    # 노드의 데이터를 '43 -> 54 -> 22'와 같이 출력


    # pos번째에 있는 노드의 data를 출력
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    # pos번째에 newNode를 생성
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # list의 길이를 구함
    def getLength(self):
        return self.nodeCount

    # list를 순회한다. list 형태로 출력
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    # list와 list를 합친다
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        elif pos==1:
            curr=self.head
            self.head=curr.next
            if self.nodeCount==1:
                self.tail=None   # 삭제 후 빈 리스트가 되기 때문에?
        else:
            prev=self.getAt(pos-1)
            curr=prev.next
            prev.next=curr.next
            if pos==self.nodeCount:
                self.tail=prev

        self.nodeCount-=1
        return curr.data

list= LinkedList()
