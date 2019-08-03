class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head1 = None
        self.head2 = None
        self.size = 0

    def push_in_stack(self, data):
        p1 = self.head1
        temp = StackNode(data)
        if p1:
            while p1.next:
                p1 = p1.next
            p1.next = temp
        else:
            self.head1 = temp
        self.size += 1

    def pop_from_stack(self):
        if self.isEmpty():
            return -1
        else:
            if self.size == 1:
                tmp = self.head1
                self.head1 = None
                self.size -= 1
                return tmp.data
            else:
                tmp = None
                p1 = self.head1
                p2 = self.head2
                next_ = None
                while p1 and self.size != 1:
                    next_ = p1.next
                    p1.next = None
                    p2 = p1
                    p1 = next_
                    self.size -= 1
                tmp = p1
                p1 = p2
                p2 = None
                return tmp.data

    def isEmpty(self):
        if self.size == 0:
            return True
        return False


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        s1 = Stack()
        while i < len(a):
            if a[i] == 1:
                s1.push_in_stack(a[i+1])
                i += 1
            else:
                print(s1.pop_from_stack(), end=" ")
            i += 1
        print()
