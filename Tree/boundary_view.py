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
            return

    def print_right(self, root):
        if root.right:
            print(root.data)
            root = root.right
            self.print_right(root)
        else:
            return

    def print_leaf(self, root):
        if root:
            self.print_leaf(root.left)
            if root.left is None and root.right is None:
                print(root.data)
            self.print_leaf(root.right)

    def printBoundary(self, root):
        print(root.data)
        self.print_left(root.left)
        self.print_leaf(root)
        self.print_right(root.right)


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
