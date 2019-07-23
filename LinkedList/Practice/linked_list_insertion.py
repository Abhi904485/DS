class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


def insertAtBegining(a, value):
    if a.head:
        first = Node(value)
        first.next = a.head
        a.head = first
    else:
        a.head = Node(value)


def insertAtEnd(a, value):
    p1 =a.head
    if p1:
        while p1.next != None:
            p1 = p1.next
        last = p1
        new_last = Node(value)
        last.next = new_last
    else:
        a.head = Node(value)


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes_info = list(map(int, input().strip().split()))
        for i in range(0, len(nodes_info)-1, 2):
            if(nodes_info[i+1] == 0):
                insertAtBegining(a, nodes_info[i])
            else:
                insertAtEnd(a, nodes_info[i])
        a.printList()
