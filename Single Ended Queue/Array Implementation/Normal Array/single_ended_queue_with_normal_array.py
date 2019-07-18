class SingleEndedQueueNormalArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.size = 0
        self.queue = [None]*self.capacity
        self.rear = -1

    def enqueue(self, item):
        if self.is_full() is True:
            print("Overflow")
        else:
            if self.front and self.rear is -1:
                self.front += 1
                self.rear += 1
                self.queue[self.rear] = item
                self.size +=1
                print("Enqueue {} in queue front = {}(index) and rear = {}(index) and size = {} ".format(
                    item, self.front, self.rear, self.size))

            elif self.rear is self.capacity-1:
                self.rear = 0
                self.queue[self.rear] = item
                self.size += 1
                print("Enqueue {} in queue front = {}(index) and rear = {}(index) and size = {} ".format(
                    item, self.front, self.rear, self.size))

            else:
                self.rear += 1
                self.queue[self.rear] = item
                self.size += 1
                print("Enqueue {} in queue front = {}(index) and rear = {}(index) and size = {} ".format(
                    item, self.front, self.rear, self.size))

    def dequeue(self):
        if self.is_empty() is True:
            print("Under flow")
        else:
            if self.front is self.capacity - 1:
                self.front = -1
                self.rear = -1
                self.size -= 1
                print("Dequeue {} from queue front = {}(index) and rear = {}(index) and size = {} ".format(
                    self.queue[self.capacity-1], self.front, self.rear, self.size))
            else:
                self.front += 1
                self.size -= 1
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


seqna = SingleEndedQueueNormalArray(5)
seqna.enqueue(1)
seqna.enqueue(2)
seqna.enqueue(3)
seqna.enqueue(4)
seqna.enqueue(5)
seqna.dequeue()
seqna.dequeue()
seqna.dequeue()
seqna.dequeue()
seqna.dequeue()
seqna.enqueue(6)
seqna.enqueue(7)
seqna.enqueue(8)
