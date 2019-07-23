
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


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


def isLengthEvenOrOdd(head):
    if head:
        count = 1
        while head.next != None:
            count += 1
            head = head.next
        return True if count % 2 == 0 else False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        if(isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')
