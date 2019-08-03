class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head_stack_1 = None
        self.head_stack_2 = None
        self.size = 0

    def enqueue(self, data):
        self.head_stack_1
        temp = QueueNode(data)
        if self.head_stack_1:
            temp.next = self.head_stack_1
            self.head_stack_1 = temp
        else:
            self.head_stack_1 = temp
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            if self.size == 1:
                tmp = self.head_stack_1
                self.head_stack_1 = None
                self.size -= 1
                return tmp.data
            else:
                tmp = None
                p1 = self.head_stack_1
                p2 = self.head_stack_2
                next_ = None
                while p1:
                    if p2:
                        tmp = p1
                        next_ = p1.next
                        tmp.next = p2
                        self.head_stack_2 = tmp
                    else:
                        tmp = p1
                        next_ = p1.next
                        tmp.next  = None
                        p2 = tmp
                    p1 = next_
                result = self.head_stack_2.data
                self.head_stack_2 = self.head_stack_2.next
                self.head_stack_1 = self.head_stack_2
                return result
                        
                    

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
        s1 = Queue()
        while i < len(a):
            if a[i] == 1:
                s1.enqueue(a[i+1])
                i += 1
            else:
                print(s1.dequeue(), end=" ")
            i += 1
        print()
