import sys
sys.path += ['.']
from SingleEndedQueue.LinkedListImplementation.node import Node


class SingleEndedQueueList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.size = 0
        self.rear = self.capacity-1
        self.head = None

    def enqueue(self, node):
        if self.is_full() is True:
            print("Over flow")

        else:
            if self.head is None:
                self.rear = (self.rear+1) % self.capacity
                self.size += 1
                self.head = node
                print("Enqueue {} front = {} , rear = {} and size = {}".format(
                    node.data, self.front, self.rear, self.size))

            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                self.rear = (self.rear+1) % self.capacity
                self.size += 1
                temp.next = node
                print("Enqueue {} front = {} , rear = {} and size = {}".format(
                    node.data, self.front, self.rear, self.size))

    def dequeue(self):
        if self.is_empty() is True:
            print("Under Flow")
        if self.head.next is None:
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            print("Dnqueue {} front = {} , rear = {} and size = {}".format(
                self.head.data, self.front, self.rear, self.size))
            self.head = None

        else:
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            temp = self.head
            print("Dnqueue {} front = {} , rear = {} and size = {}".format(
                temp.data, self.front, self.rear, self.size))
            self.head = temp.next
            temp.next = None

    def is_full(self):
        if self.size is self.capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.size is 0:
            return True
        else:
            return False

    def get_front(self):
        if self.is_empty is True:
            print("Underflow")
        else:
            return self.front

    def get_rear(self):
        if self.is_empty is True:
            print("Underflow")
        else:
            return self.rear


seql = SingleEndedQueueList(5)
seql.enqueue(Node(1))
seql.enqueue(Node(2))
seql.enqueue(Node(3))
seql.enqueue(Node(4))
seql.enqueue(Node(5))

seql.dequeue()
seql.dequeue()
seql.dequeue()
seql.enqueue(Node(6))
seql.enqueue(Node(7))
seql.enqueue(Node(8))
seql.enqueue(Node(9))