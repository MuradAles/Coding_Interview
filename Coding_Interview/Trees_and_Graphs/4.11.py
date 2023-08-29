import random


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

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, data):
        if self is None:
            return self
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            temp = self.right.find_min()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self


def random_select_node(root):
    if root is None:
        return None
    nodes = []  # To store all nodes in the tree

    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            nodes.append(node)
            inorder_traversal(node.right)

    inorder_traversal(root)
    selected_node = random.choice(nodes)
    return selected_node


def main():
    # Create a binary search tree
    root = Node(50)
    root.insert(30)
    root.insert(70)
    root.insert(20)
    root.insert(40)
    root.insert(60)
    root.insert(80)

    # Randomly select a node from the tree
    selected_node = random_select_node(root)
    if selected_node:
        print("Selected node:", selected_node.data)
    else:
        print("Tree is empty.")


if __name__ == "__main__":
    main()
