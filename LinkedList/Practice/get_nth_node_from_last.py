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


def getNthfromEnd(head, n):
    count = 0
    sp = nth = head
    while nth and count != n-1:
        nth = nth.next
        count += 1
    try:
        while nth.next != None:
            sp = sp.next
            nth = nth.next
    except:
        return -1
    return sp.data


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, nth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthfromEnd(a.head, nth_node))
