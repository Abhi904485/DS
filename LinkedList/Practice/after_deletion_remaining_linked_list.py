class node:
    def __init__(self):
        self.data = None
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node


def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)


def get_length(head):
    if head:
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count


def delNode(head, k):
    length = get_length(head)
    p1 = head
    if k == 1:
        head = head.next
    elif length == k:
        while p1.next.next != None:
            p1 = p1.next
        p1.next = None
    else:
        if p1:
            count = 1
            while p1 and count+1 != k:
                p1 = p1.next
                count += 1
            before_previous = p1
            before_ = p1.next
            before_after = before_.next
            before_previous.next = before_after
            before_.next = None
    return head
