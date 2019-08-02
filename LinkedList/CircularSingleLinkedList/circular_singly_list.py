class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList():
    def __init__(self):
        self.head = None

    def insertion_start(self, node):
        """If there is no elements in circular linked list"""
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            """if there is only one node in circular linked list"""
            if self.head.next is self.head:
                temp = self.head
                node.next = temp
                temp.next = node
                self.head = node
            else:
                """If there is more than one or two node in circular linked list"""
                temp = self.head
                node.next = temp
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = node
                self.head = node

    def insertion_specific(self, after_node_data, node):
        """If there is no elements in circular linked list"""
        if self.head is None:
            print("underflow")
        """if there is only one node in circular linked list"""
        if self.head.next is self.head:
            self.insertion_start(node)
        else:
            """If there is more than one or two node in circular linked list"""
            temp = self.head
            while temp.data is not after_node_data:
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def insertion_last(self, node):
        """If there is no elements in circular linked list"""
        if self.head is None:
            self.insertion_start(node)
        else:
            """If there is more than one or two node in circular linked list"""
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head

    def deletion_start(self):
        """If there is no elements in circular linked list"""
        if self.head is None:
            print("Unde flow")
        else:
            """if there is only one node in circular linked list"""
            if self.head.next is self.head:
                self.head = None
            else:
                """If there is more than one or two node in circular linked list"""
                fornone = self.head
                temp = self.head
                self.head = temp.next
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = self.head
                fornone.next = None

    def deletion_specific(self, node_data):
        """If there is no elements in circular linked list"""
        if self.head is None:
            print("Underflow")
        """if there is only one node in circular linked list"""
        if self.head.next is self.head:
            self.deletion_start()
        elif self.head.next.next is self.head:
            self.deletion_last()
        else:
            """If there is more than one or two node in circular linked list"""
            temp = self.head
            while temp.next.data is not node_data:
                temp = temp.next
            fornone = temp.next
            temp.next = temp.next.next
            fornone.next = None

    def deletion_last(self):
        """If there is no elements in circular linked list"""
        if self.head is None:
            print("Under flow")
        else:
            """if there is only one node in circular linked list"""
            if self.head.next is self.head:
                self.head = None
            else:
                """If there is more than one or two node in circular linked list"""
                temp = self.head
                while temp.next.next is not self.head:
                    temp = temp.next
                fornone = temp.next
                temp.next = self.head
                fornone.next = None

    def traverse(self):
        p1 = self.head
        if p1 is None:
            print("There is no element in Linked List")
        print("--" * 50)
        print("HEAD", end=" ")
        while p1.next != self.head:
            print("--->|{}||{}|".format(str(p1.data),
                                        str(p1.next.data) if p1.next else "None"), end="")
            p1 = p1.next
        print("--->|{}||{}|".format(str(p1.data), str(p1.next.data)
                                    if p1.next else "None") + " HEAD --->")
        print("--" * 50)


c1 = CircularLinkedList()
c1.insertion_start(Node(1))
print("After Insertion of Node 1 at start ")
c1.traverse()
print()
c1.insertion_start(Node(2))
print("After Insertion of Node 2 at start ")
c1.traverse()
print()
c1.insertion_start(Node(3))
print("After Insertion of Node 3 at start ")
c1.traverse()
print()
c1.insertion_specific(2, Node(4))
print("After Insertion of Node 4 at postion 2")
c1.traverse()
print()
c1.insertion_last(Node(5))
print("After Insertion of Node 5 at postion last")
c1.traverse()
print()
