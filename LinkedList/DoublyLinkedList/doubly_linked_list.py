class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():

    def __init__(self):
        self.head = None

    def insertion_start(self, node):
        if self.head is None:
            self.head = node

        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def insertion_end(self, node):
        if self.head is None:
            self.insertion_start(node)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            node.previous = temp
            temp.next = node

    def insertion_specific(self, after_node_data, node):
        if self.head and self.head.next is None:
            print("Minimum two elements are there for insertion in specific position")
        else:
            temp = self.head
            temp1 = temp.next
            while temp.data is not after_node_data:
                temp = temp.next
            node.previous = temp
            node.next = temp1
            temp1.previous = node
            temp.next = node

    def deletion_start(self):
        if self.head is None:
            print("Under flow")
        else:
            temp = self.head
            fornone = self.head
            self.head = temp.next
            temp.next = None
            self.head.previous = None
            """For freeing up node"""
            fornone.next = None
            fornone.previous = None

    def deletion_specific(self, node_data):
        if self.head and self.head.next and self.head.next.next is None:
            print("Minimum Three elements are there for deletion at specific location")

        else:
            temp = self.head
            while temp.data is not node_data:
                temp = temp.next
            fornone = temp
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            """For freeing up node"""
            fornone.previous = None
            fornone.next = None

    def deletion_end(self):
        if self.head is None:
            print("Under flow")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            fornone = temp
            temp.previous.next = None
            temp.previous = None
            """For freeing up node"""
            fornone.next = None
            fornone.previous = None

    def traverse(self):
        p1 = self.head
        if p1 is None:
            print("There is no element in Linked List")
        print("--" * 50)
        print("HEAD", end=" ")
        while p1 is not None:
            print("--->|{}||{}||{}|".format(str(p1.previous.data) if p1.previous else "None", str(p1.data),
                                            str(p1.next.data) if p1.next else "None"), end="")
            p1 = p1.next
        print()
        print("--" * 50)


d1 = DoublyLinkedList()
d1.insertion_start(Node(1))
print("After Insertion 1 at start")
d1.traverse()
print()
d1.insertion_start(Node(2))
print("After Insertion 2 at start ")
d1.traverse()
print()
d1.insertion_end(Node(3))
print("After Insertion 3 at end")
d1.traverse()
print()
d1.insertion_specific(2, Node(4))
print("Insertion of 4 at second position ")
d1.traverse()
print()
d1.deletion_specific(1)
print("After deletion of  Node at position 1")
d1.traverse()
print()
