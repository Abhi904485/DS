
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
            # arr.append(str(temp.data))
            temp = temp.next
        print()

# Recursive Solution
def delete_greater_node_right(head):
    if head.next == None:
        return head 
    temp = delete_greater_node_right(head.next)
    if temp.data > head.data:
        return temp
    else:
        head.next = temp
    return head 


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        # k = int(input())
        new_head = LinkedList()
        new_head = delete_greater_node_right(llist.head)
        llist.head = new_head
        llist.printList()
        t -= 1
