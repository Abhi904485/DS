
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


def length(head):
    if head:
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count


def sum_last_n_node_data(head, k):
    sum_ = 0
    count = 0
    nth = head
    move = length(head)
    while count != (move-k):
        nth = nth.next
        count += 1
    while k:
        sum_ += nth.data
        nth = nth.next
        k -= 1
    return sum_


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        new_head = LinkedList()
        sum_ = sum_last_n_node_data(llist.head, k)
        print(sum_)
        t -= 1
