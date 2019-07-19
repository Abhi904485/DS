class DoublyEndedQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.size = 0
        self.rear = -1
        self.queue = [None]*self.capacity

    def enqueue_front(self, item):
        if self.is_full() is True:
            print("Overflow")

        else:
            """If there is no Element in Queue"""
            if self.front and self.rear is -1:
                self.front += 1
                self.rear += 1

            
            elif self.front is 0:
                """If front is pointing to zeroth index of queue and queue is empty """
                self.front = self.capacity - 1

            else:
                """If more than one element in Queue"""
                self.front -= 1
            self.queue[self.front] = item
            self.size += 1
            print("Enqueue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                item, self.front, self.rear, self.size))

    def enqueue_rear(self, item):
        if self.is_full() is True:
            print("Overflow")
        else:
            """If there is no Element in Queue"""
            if self.front and self.rear is -1:
                self.front += 1
                self.rear += 1
            elif self.rear is self.capacity-1:
                """If rear is pointing to last index of queue and queue is empty """
                self.rear = 0

            else:
                """If more than one element in Queue"""
                self.rear += 1

            self.queue[self.rear] = item
            self.size += 1
            print("Enqueue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                item, self.front, self.rear, self.size))

    def dequeue_front(self):
        if self.is_empty is True:
            print("Underflow")

        elif self.front is self.capacity-1:
            """if front is pointing to last index of queue """
            self.size -= 1
            print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                self.queue[self.front], self.front, self.rear, self.size))
            self.front = 0
        else:
            """if front is pointing to any middle index of queue"""
            self.front += 1
            self.size -= 1
            print("Dequeue {} from front and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                self.queue[self.front-1], self.front, self.rear, self.size))

    def dequeue_rear(self):
        if self.is_empty is True:
            print("Underflow")

        else:
            """if rear is pointing to zeroth location of queue"""
            if self.rear is 0:
                self.size -= 1
                print("Dequeue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    self.queue[self.rear], self.front, self.rear, self.size))
                self.rear = self.capacity-1

            else:
                """if rear is pointing to any middle location of queue """
                self.rear -= 1
                self.size -= 1
                print("Dequeue {} from rear and front location = {}(index) , rear location = {}(index) and size = {} ".format(
                    self.queue[self.rear+1], self.front, self.rear, self.size))

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


deqa = DoublyEndedQueueArray(5)
# deqa.enqueue_front(1)
# deqa.enqueue_front(2)
# deqa.enqueue_front(3)
# deqa.enqueue_front(4)
deqa.enqueue_rear(1)
deqa.enqueue_rear(2)
deqa.enqueue_rear(3)
deqa.enqueue_rear(4)
deqa.enqueue_rear(5)
deqa.dequeue_front()
deqa.dequeue_rear()
# deqa.enqueue_rear(1)
