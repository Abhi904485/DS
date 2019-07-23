
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked list class


class LinkedList:
    def __init__(self):
        self.head = None
    # append at the end of the list

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


def getCount(head_node):
    count = 0
    while head_node != None:
        head_node = head_node.next
        count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        # list containing nodes
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            node = Node(x)  # create a new node
            a.append(node)
        print(getCount(a.head))
