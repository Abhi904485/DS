
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


def getNth(head, k):
    count = 1
    if head:
        while count != k:
            head = head.next
            count += 1
        return head.data


if __name__ == '__main__':
    llist = LinkedList()
    T = int(input())
    while (T > 0):
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        value = list(map(int, input().split()))
        for i in reversed(value):
            llist.push(int(i))
        m = getNth(llist.head, k)
        print(m)
        T -= 1
