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

    def getNode(self, value):  # return node with given value, if not present return None
        curr_node = self.head
        while(curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if(curr_node.data == value):
            return curr_node
        else:
            return None
    # prints the elements of linked list starting with head

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


my_list = []


def deleteNode(curr_node):
    prev = None
    while curr_node.next:
        curr_node.data = curr_node.next.data
        prev = curr_node
        curr_node = curr_node.next
    prev.next = None
  

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        del_elem = int(input())
        to_delete = a.getNode(del_elem)
        deleteNode(to_delete)
        a.printList()
