class my_stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
        self.size = 0
        self.max_element = None
        self.track_stack = []

    def push_stack(self, item):
        if self.is_full() is True:
            print("Overflow")
        else:
            self.stack.insert(0, item)
            self.size += 1
            if self.max_element is None:
                self.track_stack.insert(0, item)
                self.max_element = item
            elif self.max_element <= item:
                self.track_stack.insert(0, item)
                self.max_element = item
            print("Max element = {} ".format(self.max_element))

    def pop_stack(self):
        if self.is_empty is True:
            print("Underflow")
        else:
            self.size -= 1
            item = self.stack[0]
            if self.track_stack[0] == item:
                self.track_stack.remove(item)
                try:
                    print("Max element = {} ".format(self.track_stack[0]))
                except:
                    pass
            return self.stack.pop(0)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_top_element(self):
        return self.stack[0]

    def is_full(self):
        if self.size is self.capacity:
            return True
        else:
            return False


s1 = my_stack(10)
s1.push_stack(1)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(9)
s1.push_stack(10)

print("Abhishek")


s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()
s1.pop_stack()