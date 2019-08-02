class MyQueue:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, item):
        self.arr.insert(0, item)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return -1
        self.size -= 1
        return self.arr.pop()

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
