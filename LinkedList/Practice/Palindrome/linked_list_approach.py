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


def traverse_start(head):
    result = ""
    p1 = head
    while p1:
        result += str(p1.data)
        p1 = p1.next
    return result


def traverse_last(head):
    p1 = head
    if not p1.next:
        return str(p1.data)
    return traverse_last(p1.next)+str(p1.data)


def isPalindrome(head):
    s1 = traverse_start(head)
    s2 = traverse_last(head)
    print(s1)
    print(s2)
    if s1 == s2:
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
