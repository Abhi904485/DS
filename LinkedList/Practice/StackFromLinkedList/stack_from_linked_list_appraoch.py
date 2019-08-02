class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        if self.head:
            temp = StackNode(data)
            temp.next = self.head
            self.head = temp
        else:
            self.head = StackNode(data)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            if self.size == 1:
                tmp = self.head
                self.head = None
                self.size -= 1
                return tmp.data
            else:
                self.size -= 1
                tmp = self.head
                self.head = self.head.next
                tmp.next = None
                return tmp.data

    def isEmpty(self):
        if self.size == 0:
            return True
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
