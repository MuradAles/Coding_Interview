class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(" " * 4 * level + "-> " + str(node.data))
        printTree(node.right, level + 1)


def BST(array):
    if not array:
        return
    # odd length
    if len(array) % 2 != 0:
        middle_num = array[(len(array)) // 2]
    # even length
    if len(array) % 2 != 1:
        middle_num = array[(len(array) - 1) // 2]
    print(middle_num)
    root = Node(middle_num)
    for i in array:
        root.insert(i)
    return root


def main():
    sorted_array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root_1 = BST(sorted_array_1)
    root_2 = BST(sorted_array_2)
    printTree(root_1)
    print("---------------")
    printTree(root_2)


main()
