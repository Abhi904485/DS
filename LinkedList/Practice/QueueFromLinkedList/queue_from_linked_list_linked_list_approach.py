class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        if self.head:
            temp = Node(item)
            temp.next = self.head
            self.head = temp
        else:
            self.head = Node(item)
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
                p1 = self.head
                self.size -= 1
                while p1.next.next:
                    p1 = p1.next
                tmp = p1.next
                p1.next = None
                return tmp.data

    def isEmpty(self):
        if self.size == 0:
            return True
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i+1])
                i = i+2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i+1
            elif(s.isEmpty()):
                print(-1)
                i = i+1
        print()
