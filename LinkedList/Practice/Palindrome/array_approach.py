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
# returns the size of linked list


def getSize(head):
    count = 0
    curr_node = head
    while curr_node:
        count += 1
        curr_node = curr_node.next
    return count


def isPalindrome(head):
    my_str = ""
    p1 = head
    if p1:
        while p1:
            my_str += str(p1.data)
            p1 = p1.next
        if my_str == my_str[::-1]:
            return True
        return False


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
