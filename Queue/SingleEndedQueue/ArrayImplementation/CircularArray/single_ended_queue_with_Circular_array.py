class SingleEndedQueueCircularArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.size = 0
        self.queue = [None]*self.capacity
        self.rear = self.capacity-1

    def enqueue(self, item):
        if self.is_full() is True:
            print("Overflow")
        else:
            self.rear = (self.rear+1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
            print("Enqueue {} in queue front = {}(index) and rear = {}(index) and size = {} ".format(
                item, self.front, self.rear, self.size))

    def dequeue(self):
        if self.is_empty() is True:
            print("Under flow")

        else:
            self.size -= 1
            self.front = (self.front+1) % self.capacity
            print("Dequeue {} from queue front = {}(index) and rear = {}(index) and size = {} ".format(
                self.queue[self.front-1], self.front, self.rear, self.size))

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


seqa = SingleEndedQueueCircularArray(5)
seqa.enqueue(1)
seqa.enqueue(2)
seqa.enqueue(3)
seqa.enqueue(4)
seqa.enqueue(5)
seqa.dequeue()
seqa.dequeue()
seqa.enqueue(6)
seqa.enqueue(7)
seqa.enqueue(8)
