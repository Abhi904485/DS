import sys
sys.path += ['.']
from LinkedList.SingleLinkedList.node import Node

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def insertion_start(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = node
            temp.next = self.head
            self.head = temp

    def insertion_specific(self, after_node_data, node):
        if self.head and self.head.next is None:
            print("Under flow")
        else:
            temp = self.head
            while temp.data is not after_node_data:
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def insertion_last(self, node):
        if self.head is None:
            self.insertion_start(node)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.next = None

    def deletion_start(self):
        if self.head is None:
            print("Under flow")
        else:
            temp = self.head
            fornone = self.head
            self.head = temp.next
            temp.next = None
            """For freeing up Node"""
            fornone.next = None

    def deletion_specific(self, after_node_data):
        if self.head and self.head.next and self.head.next.next is None:
            print("Underflow")
        else:
            temp = self.head
            while temp.data is not after_node_data:
                temp = temp.next
            fornone = temp
            temp.next = temp.next.next
            """For freeing up Node"""
            fornone.next = None

    def deletion_end(self):
        if self.head is None:
            print("under flow")
        elif self.head.next is None:
            self.head = None
            print("There is only one element in linked list we delete that one also")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            """Freeing up node logic is already included in below statement"""
            temp.next = None

    def traverse_list(self):
        p1 = self.head
        if p1 is None:
            print("There is no element in Linked List")
        print("--" * 50)
        print("HEAD",end = " ")
        while p1 is not None:
            print("--->|{}||{}|".format(str(p1.data),
                                        str(p1.next.data) if p1.next else "None"), end="")
            p1 = p1.next
        print()
        print("--" * 50)

    def reverse_linked_list(self , p1):
        if p1.next == None:
            self.head = p1
            return self.head
        current = p1
        next_ = current.next
        self.reverse_linked_list(next_)
        next_.next = current
        current.next = None

    def get_head(self):
        return self.head


l1 = SingleLinkedList()
l1.insertion_start(Node(1))
print("After Insertion 1 at start")
l1.traverse_list()
print()
print("Linked List Reversed ")
l1.reverse_linked_list(l1.get_head())
l1.traverse_list()
print()
l1.insertion_start(Node(2))
print("After Insertion 2 at start")
l1.traverse_list()
print()
print("Linked List Reversed ")
l1.reverse_linked_list(l1.get_head())
l1.traverse_list()
print()
l1.insertion_specific(1, Node(4))
print("After Insertion of Node 4 at postion 1 ")
l1.traverse_list()
print()
print("Linked List Reversed ")
l1.reverse_linked_list(l1.get_head())
l1.traverse_list()
print()
l1.insertion_last(Node(3))
print("After Insertion of Node 3 at postion last")
l1.traverse_list()
print()
print("Linked List Reversed ")
l1.reverse_linked_list(l1.get_head())
l1.traverse_list()
print()
l1.deletion_specific(1)
print("After Deletion at postion 1 ")
l1.traverse_list()
print()
print("Linked List Reversed ")
l1.reverse_linked_list(l1.get_head())
l1.traverse_list()
print()
