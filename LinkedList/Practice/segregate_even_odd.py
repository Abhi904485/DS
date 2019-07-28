
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


def segregate_even_odd(head):
    p1 = head
    odd = None
    even = None
    even_last = None
    odd_last = None
    while p1:
        if p1.data % 2 == 0:
            if not even:
                even = p1
                rem = even.next
                even.next = None
                even_last = p1

            else:
                even_last.next = p1
                rem = p1.next
                p1.next = None
                even_last = p1

        else:
            if not odd:
                odd = p1
                rem = odd.next
                odd.next = None
                odd_last = p1

            else:
                odd_last.next = p1
                rem = p1.next
                p1.next = None
                odd_last = p1

        p1 = rem

    if not p1:
        if even and not odd:
            head = even
        elif not even and odd:
            head = odd
        else:
            if even_last:
                head = even
                even_last.next = odd
            else:
                head = even
                head.next = odd
    return head


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        new_head = LinkedList()
        new_head = segregate_even_odd(llist.head)
        llist.head = new_head
        llist.printList()
        t -= 1
