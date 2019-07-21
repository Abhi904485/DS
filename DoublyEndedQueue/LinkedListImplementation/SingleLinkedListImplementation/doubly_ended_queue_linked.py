import sys
sys.path += ['.']

from DoublyEndedQueue.LinkedListImplementation.SingleLinkedListImplementation.node import Node


class DoublyEndedQueueSingleLinked:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.size = 0
        self.head = None

    def enqueue_front(self, node):
        if self.is_full() is True:
            print("Overflow")

        else:
            """If there is no Element in Queue"""
            if self.front and self.rear is -1:
                self.front += 1
                self.rear += 1
                self.size += 1
                self.head = node
                print("Enqueue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

            elif self.front is 0:
                self.front = self.capacity - 1
                self.size += 1
                self.head.next = node
                print("Enqueue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

            else:
                """If more than one element in Queue"""
                self.front -= 1
                temp = self.head
                while temp.next is not None:
                    temp = temp .next
                temp.next = node
                self.size += 1
                print("Enqueue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

    def enqueue_rear(self, node):
        if self.is_full() is True:
            print("Overflow")
        else:
            """If there is no Element in Queue"""
            if self.front and self.rear is -1:
                self.front += 1
                self.rear += 1
                self.size += 1
                self.head = node
                print("Enqueue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

            elif self.rear is self.capacity-1:
                """If rear is pointing to last index of queue and queue is empty """
                self.rear = 0
                self.size += 1
                self.head.next = node
                print("Enqueue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

            else:
                """If more than one element in Queue"""
                self.rear += 1
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = node
                self.size += 1
                print("Enqueue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    node.data, self.front, self.rear, self.size))

    def dequeue_front(self):
        if self.is_empty is True:
            print("Underflow")

        else:
            if self.front is self.rear and self.size is 1:
                """if front is pointing to last index of queue """
                self.front = -1
                self.rear = -1
                self.size = 0
                temp =self.head
                print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                self.head = None

            elif self.front is self.capacity-1:
                self.front = 0
                self.size -= 1
                temp = self.head
                self.head = temp.next
                print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                temp = None

            else:
                self.front += 1
                self.size -= 1
                temp = self.head
                self.head = temp.next
                print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                temp = None

    def dequeue_rear(self):
        if self.is_empty is True:
            print("Underflow")

        else:
            """if rear is pointing to zeroth location of queue"""
            if self.front is self.rear and self.size is 1:
                self.front = -1
                self.rear = -1
                self.size = 0
                temp = self.head
                print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                self.head = None

            elif self.rear is 0:
                self.rear = self.capacity-1
                self.size -= 1
                temp = self.head
                self.head = temp.next
                print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                temp = None

            else:
                """if rear is pointing to any middle location of queue """
                self.rear -= 1
                self.size -= 1
                temp = self.head
                self.head = temp.next
                print("Dequeue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    temp.data, self.front, self.rear, self.size))
                temp = None

    def get_front(self):
        if self.is_empty() is True:
            print("Under flow")
        else:
            return self.front

    def get_rear(self):
        if self.is_empty() is True:
            print("Under flow")
        else:
            return self.rear

    def is_empty(self):
        if self.size is 0:
            return True

        else:
            return False

    def is_full(self):
        if self.size is self.capacity:
            return True
        else:
            return False


deqsl = DoublyEndedQueueSingleLinked(5)
# deqsl.enqueue_rear(Node(1))
# deqsl.enqueue_rear(Node(2))
# deqsl.enqueue_rear(Node(3))
# deqsl.enqueue_rear(Node(4))
# deqsl.enqueue_rear(Node(5))
# deqsl.dequeue_rear()
# deqsl.dequeue_rear()
# deqsl.dequeue_rear()
# deqsl.dequeue_rear()
# deqsl.dequeue_rear()

deqsl.enqueue_front(Node(1))
deqsl.enqueue_front(Node(2))
deqsl.enqueue_front(Node(3))
deqsl.enqueue_front(Node(4))
deqsl.enqueue_front(Node(5))
deqsl.dequeue_front()
deqsl.dequeue_front()
deqsl.dequeue_front()
deqsl.dequeue_front()
deqsl.dequeue_front()