class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(" " * 4 * level + "-> " + str(node.data))
        printTree(node.right, level + 1)


def main():
    root_1 = TreeNode(50)
    root_1.left = TreeNode(40)
    root_1.right = TreeNode(60)
    root_1.left.left = TreeNode(30)
    root_1.left.right = TreeNode(35)
    root_1.right.left = TreeNode(65)
    root_1.right.right = TreeNode(70)
    root_1.right.left = TreeNode(65)
    root_1.right.right.right = TreeNode(75)
    printTree(root_1)
    print("-----------------")
    root_2 = TreeNode(50)
    root_2.left = TreeNode(40)
    root_2.right = TreeNode(60)
    root_2.right.left = TreeNode(65)
    root_2.right.right = TreeNode(70)
    root_2.right.left = TreeNode(65)
    root_2.right.right.right = TreeNode(75)
    printTree(root_2)


main()
