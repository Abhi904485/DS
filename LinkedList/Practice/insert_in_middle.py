
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


def insertInMid(head, node):
    if head.next == None:
        head.next = node
    elif head.next.next == None:
        t1 = head.next
        head.next = node
        node.next = t1
    else:
        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        t1 = sp.next
        sp.next = node
        node.next = t1
    return head




if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = Node(int(input()))
        new_head = LinkedList()
        new_head = insertInMid(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
