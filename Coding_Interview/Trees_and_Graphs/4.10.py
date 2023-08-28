class Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree_Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree_Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def isSubtree(self, root, subRoot) -> bool:
        def preorder(root):
            if root is None:
                return False
            if check(root, subRoot):
                return True
            return preorder(root.left) or preorder(root.right)

        def check(root, subRoot):
            if not root and not subRoot:
                return True
            if (
                root
                and subRoot
                and root.data == subRoot.data
                and check(root.left, subRoot.left)
                and check(root.right, subRoot.right)
            ):
                return True
            return False

        return preorder(root)


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(" " * 4 * level + "-> " + str(node.data))
        printTree(node.right, level + 1)


def main():
    root_1 = Tree_Node(10)
    root_1.insert(5)
    root_1.insert(1)
    root_1.insert(12)
    root_1.insert(7)
    root_1.insert(28)
    root_1.insert(11)
    root_1.insert(45)
    printTree(root_1)
    root_2 = Tree_Node(5)
    root_2.insert(1)
    root_2.insert(7)
    printTree(root_2)
    print(root_1.isSubtree(root_1, root_2))


main()
