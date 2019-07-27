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
    temp = head
    size = cal_size(head)
    if size <= k:
        pass
    else:
        # while temp.next!=None:
        #     temp = temp.next
        # temp.next = head
        end = None
        while k>0:
            end = head
            head = head.next
            k -=1
        end.next = None
        return temp , head
        

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
