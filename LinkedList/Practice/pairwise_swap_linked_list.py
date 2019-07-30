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
            # arr.append(str(temp.data))
            temp = temp.next
        print()


def pairWiseSwap(head):
    head = reverse(head, 2)
    return head


def reverse(head, k):
    if head == None:
        return head
    count = 0
    previous = None
    current = head
    while current and count < k:
        next_ = current.next
        current.next = previous
        previous = current
        current = next_
        count += 1
    if previous:
        head.next = reverse(next_, k)
    return previous


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        llist.head = pairWiseSwap(llist.head)
        llist.printList()
        t -= 1
