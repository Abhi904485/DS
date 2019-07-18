class my_stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
        self.size = 0
        self.max_element = None

    def push_stack(self, item):
        if self.is_full() is True:
            print("Overflow")
        else:
            self.stack.insert(0, item)
            self.size += 1
            
    def pop_stack(self):
        if self.is_empty is True:
            print("Underflow")
        else:
            self.size -= 1
            return self.stack.pop()

    def reverse_stack(self):
        if self.is_empty() is not True:
            temp = self.pop_stack()
            self.reverse_stack()
            self.push_stack(temp)

    def print_stack(self):
        for item in self.stack:
            print(str(item)+"---->", end=" " )

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

    def track_max(self, item):
        if self.is_empty():
            print("Under flow")

        else:
            if self.max_element is None:
                return item
            else:
                if self.max_element < item:
                    return item
                else:
                    return self.max_element



s1 = my_stack(10)
s1.push_stack(1)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(7)
s1.push_stack(2)
s1.push_stack(2)
s1.push_stack(10)
print("print before Reverse of stack")
s1.print_stack()
s1.reverse_stack()
print("\n")
print("print After Reverse of stack")
s1.print_stack()
