class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    # prints the elements of linked list starting with head

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


def merge(head_a, head_b):
    p1 = head_a
    p2 = head_b
    temp = None
    last = None
    while p1 and p2 and not temp:
        if p1.data < p2.data:
            temp = p1
            last = p1
            p1 = p1.next
        else:
            temp = p2
            last = p2
            p2 = p2.next

    while p1 and p2 and temp:
        if p1.data < p2.data:
            last.next = p1
            last = p1
            p1 = p1.next
        else:
            last.next = p2
            last = p2
            p2 = p2.next

    if p1:
        last.next = p1
    if p2:
        last.next = p2

    return temp


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, m = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        for x in nodes_b:
            b.append(x)
        a.head = merge(a.head, b.head)
        a.printList()
