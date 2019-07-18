class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class MyTree:
    def print_left(self, root):
        if root.left:
            print(root.data)
            root = root.left
            self.print_left(root)
        else:
            if root.left is None and root.right is None:
                print(root.data)

    def printBoundary(self, root):
        print(root.data)
        self.print_left(root.left)

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.left = Node(21)
root.right.right = Node(25)

m1 = MyTree()
m1.printBoundary(root)