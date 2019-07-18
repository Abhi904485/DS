from node import Node


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
                fornone  = self.head
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
            fornone  = temp.next
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
                fornone.next  = None
    

    def traverse(self):
        """If there is no elements in circular linked list"""
        if self.head is None:
            print("Under flow")
        else:
            temp = self.head
            while temp.next is not self.head:
                print(str(temp.data)+"--->", end="")
                temp = temp.next
            print(str(temp.data)+"--->", end="")


c1 = CircularLinkedList()
c1.insertion_start(Node(1))
c1.insertion_start(Node(2))
c1.insertion_start(Node(3))
c1.insertion_specific(2, Node(4))
c1.insertion_last(Node(5))
# c1.deletion_start()
c1.deletion_last()
# c1.deletion_specific(4)
c1.traverse()
