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
        while(temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")


def cal_size(head):
    p1 = head
    if p1:
        count = 1
        while p1.next != None:
            p1 = p1.next
            count += 1
    return count


def rotateList(head, k):
    first_head = head
    size = cal_size(head)
    count = 0
    if size <= k:
        return head
    else:
        while count < k-1:
            first_head = first_head.next
            count += 1
        second_first_node = first_head.next
        first_head.next = None
        first_head = head
        second_first_node_temp = second_first_node
        while second_first_node_temp.next != None:
            second_first_node_temp = second_first_node_temp.next
        second_first_node_temp.next = first_head
        head = second_first_node
    return head


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
