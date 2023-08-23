class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isValidBST(self, root, min_val=float("-inf"), max_val=float("inf")) -> bool:
        if not root:
            return True

        if root.data <= min_val or root.data >= max_val:
            return False

        left_valid = self.isValidBST(root.left, min_val, root.data)
        right_valid = self.isValidBST(root.right, root.data, max_val)

        return left_valid and right_valid


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(" " * 4 * level + "-> " + str(node.data))
        printTree(node.right, level + 1)


def main():
    root_bst = Node(10)
    root_bst.left = Node(5)
    root_bst.right = Node(15)
    # left
    root_bst.left.left = Node(3)
    root_bst.left.right = Node(7)
    # right
    root_bst.right.left = Node(13)
    root_bst.right.right = Node(17)
    # left left 3
    root_bst.left.left.left = Node(2)
    root_bst.left.left.right = Node(4)
    # left Right 7
    root_bst.left.right.left = Node(6)
    root_bst.left.right.right = Node(8)
    # Right left 13
    root_bst.right.left.left = Node(12)
    root_bst.right.left.right = Node(14)
    # Right Right 17
    root_bst.right.right.left = Node(16)
    root_bst.right.right.right = Node(11)
    printTree(root_bst)
    print(root_bst.isValidBST(root_bst))


main()
