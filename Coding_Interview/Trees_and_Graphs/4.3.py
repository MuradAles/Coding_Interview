class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def binary_tree_to_linked_lists(root):
    if not root:
        return []

    result = []
    current_level = [root]

    while current_level:
        next_level = []
        head = tail = None

        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if not head:
                head = tail = LinkedListNode(node.value)
            else:
                tail.next = LinkedListNode(node.value)
                tail = tail.next

        result.append(head)
        current_level = next_level

    return result


# Example usage
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

linked_lists = binary_tree_to_linked_lists(root)
for level_list in linked_lists:
    current = level_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
