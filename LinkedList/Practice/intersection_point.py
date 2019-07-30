class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


def length(head):
    if head:
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count


def intersetPoint(head_a, head_b):
    l1 = length(head_a)
    l2 = length(head_b)
    diff = abs(l1-l2)
    while diff:
        if l1 > l2:
            head_a = head_a.next
        else:
            head_b = head_b.next
        diff -= 1
    while True:
        if head_a.data == head_b.data:
            return head_a
        head_a = head_a.next
        head_b = head_b.next
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))
        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list
        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list
        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                # add to the end of the list b, only the intersection
                b.append(node)
        if intersetPoint(a.head, b.head) == -1:
            print(-1)
        else:
            # print data present at the node.
            print(intersetPoint(a.head, b.head).data)
