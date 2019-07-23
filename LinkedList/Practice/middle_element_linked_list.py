
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


def length(head):
    if head:
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count


def findMid(head):
    if head:
        t1= t2 = head
        if length(head) % 2 == 0:
            try:
                while t2 != None:
                    t1 = t1.next
                    t2 = t2.next.next
                return t1
            except:
                return t1
        else:
            try:
                while t2.next != None:
                    t1 = t1.next
                    t2 = t2.next.next
                return t1
            except:
                return t1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)
