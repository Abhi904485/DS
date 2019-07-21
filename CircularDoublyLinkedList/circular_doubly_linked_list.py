import sys
sys.path += ['.']
from CircularDoublyLinkedList.node import Node


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertion_start(self, node):
        """If there is no element in list"""
        if self.head is None:
            self.head = node
            node.next = node
            node.pre = node
        else:
            """If there is only one element in list"""
            if self.head.next is self.head:
                temp = self.head
                node.next = temp
                temp.pre = node
                temp.next = node
                node.pre = temp
                self.head = node
            else:
                """If there is more than one node in list"""
                temp = self.head
                node.next = temp
                temp.pre = node
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = node
                node.pre = temp
                self.head = node

    def insertion_specific(self, after_node_data, node):
        """If there is no element in list"""
        if self.head is None:
            print("undeflow")
        """If there is only one element in list"""
        if self.head.next is self.head:
            self.insertion_last(node)
        else:
            """If there is more than one node in list"""
            temp = self.head
            while temp.data is not after_node_data:
                temp = temp.next
            node.pre = temp
            node.next = temp.next
            temp.next = node
            temp.next.pre = node

    def insertion_last(self, node):
        """If there is no element in list"""
        if self.head is None:
            print("Under flow")
        else:
            """If there is more than one node in list"""
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            temp1 = temp.next
            node.next = temp1
            node.pre = temp
            temp.next = node
            self.head.pre = node

    def deletion_start(self):
        """If there is no element in list"""
        if self.head is None:
            print("Under flow")
        else:
            fornone = self.head
            """If there is more than one node in list"""
            temp = self.head
            temp1 = self.head.next
            while temp.next is not self.head:
                temp = temp.next
            temp.next = self.head.next
            temp1.pre = temp
            self.head = temp1
            """Freeing up Node"""
            fornone.next = None
            fornone.pre = None

    def deletion_specific(self, node_data):
        """If there is no element in list"""
        if self.head is None:
            print("Under flow")

        """If there is only one element in list"""
        if self.head.next is self.head:
            self.deletion_start()

        elif self.head.next.next is self.head:
            self.deletion_last()

        else:
            """If there is more than one node in list"""
            temp = self.head
            while temp.data is not node_data:
                temp = temp.next
            fornone = temp
            temp.pre.next = temp.next
            temp.next.pre = temp.pre
            """Freeing up Node"""
            fornone.next = None
            fornone.pre = None

    def deletion_last(self):
        """If there is no element in list"""
        if self.head is None:
            print("Under flow")
        """If there is only one element in list"""
        if self.head.next is self.head:
            self.head = None
        else:
            """If there is more than one node in list"""
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            fornone = temp
            temp1 = temp.next
            temp.pre.next = temp1
            self.head.pre = temp.pre.next
            """Freeing up Node"""
            fornone.next = None
            fornone.pre = None

    def traverse(self):
        p1 = self.head
        if p1 is None:
            print("There is no element in Linked List")
        print("--" * 50)
        print("HEAD", end=" ")
        while p1.next != self.head:
            print("--->|{}||{}||{}|".format(str(p1.pre.data) if p1.pre else "None", str(p1.data),
                                            str(p1.next.data) if p1.next else "None"), end="")
            p1 = p1.next
        print("--->|{}||{}||{}|".format(str(p1.pre.data) if p1.pre else "None", str(p1.data),
                                        str(p1.next.data) if p1.next else "None") + " HEAD --->")
        print("--" * 50)


cd1 = CircularDoublyLinkedList()
cd1.insertion_start(Node(1))
print("After Inserting Node 1 at start ")
cd1.traverse()
print()
cd1.insertion_start(Node(2))
print("After Inserting Node 2 at start ")
cd1.traverse()
print()
cd1.insertion_start(Node(3))
print("After Inserting Node 3 at start ")
cd1.traverse()
print()
cd1.insertion_last(Node(4))
print("After Inserting Node 4 at last ")
cd1.traverse()
print()
cd1.insertion_specific(2, Node(5))
print("After Inserting Node 5 at second Postion ")
cd1.traverse()
print()
cd1.deletion_start()
print("After Deletion of Node from start postion ")
cd1.traverse()
print()
