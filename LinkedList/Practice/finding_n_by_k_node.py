import math as m


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def fractionalNodes(self, k):
        count = m.ceil(self.size / k)
        temp = self.head
        count -= 1
        while count:
            temp = temp.next
            count -= 1
        return temp


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        #head = createList(arr, n)
        for i in range(0, len(arr)):
            lis.insert(arr[i])
        ans = lis.fractionalNodes(k)
        print(ans.data)
