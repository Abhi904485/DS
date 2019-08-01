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


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


def segregate(head):
    p1 = head
    zero = one = two = last_0 = last_1 = last_2 = None
    while p1:
        first = p1
        second = p1.next
        first.next = None
        if p1.data == 0:
            if zero:
                last_0.next = first
                last_0 = first
            else:
                zero = first
                last_0 = first
        elif p1.data == 1:
            if one:
                last_1.next = first
                last_1 = first
            else:
                one = first
                last_1 = first
        else:
            if two:
                last_2.next = first
                last_2 = first
            else:
                two = first
                last_2 = first
        p1 = second
    if two:
        head = two
    if one:
        last_1.next = head
        head = one
    if zero:
        last_0.next = head
        head = zero
    return head


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        a.head = segregate(a.head)
        printList(a.head)
