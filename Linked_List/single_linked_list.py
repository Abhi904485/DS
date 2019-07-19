import sys
sys.path += ['.']

from Linked_List.node import Node


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
            fornone.next =None

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
           fornone.next =None
            
    
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
        print("Traversing Start")
        if self.head is None:
            print("There is no element in Linked List")

        while self.head is not None:
            print(str(self.head.data)+"--->", end="")
            self.head = self.head.next


l1 = SingleLinkedList()
l1.insertion_start(Node(1))
l1.insertion_start(Node(2))
l1.insertion_specific(1,Node(4))
l1.insertion_last(Node(3))
l1.deletion_specific(1)
l1.traverse_list()
