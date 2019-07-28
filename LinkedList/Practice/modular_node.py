
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

def length(head):
    if head:
        count = 1
        while head.next != None:
            head = head.next
            count += 1
        return count

def modular_node_not_optimized(head, k):
    size  = length(head)
    my_list = [0]*size
    count = 0
    while head != None:
        my_list[count] = head.data
        head = head.next
        count += 1
    for i in range(0,size+1):
        if (size - i) % k == 0:
            head  = Node(my_list[size - i-1])
            return head


def modular_node_optimized(head, k):
    temp = head
    n = 0
    ans = None
    while temp != None:
        n += 1
        if n % k == 0:
            ans = temp
        temp = temp.next

    return ans


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = modular_node_optimized(llist.head, k)
        print(new_head.data)
        t -= 1
