class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        if not self.head:
            return
        current = self.head
        while current.next:
            print(f"{current.data}", end="->")
            current = current.next
        print(f"{current.data}")


def check_intersection(node_1, node_2):
    first_node = node_1.head
    second_node = node_2.head

    while first_node != second_node:
        first_node = node_1 if first_node is None else first_node.next
        second_node = node_2 if second_node is None else second_node.next
    return first_node


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(4)
    node1.insert_at_beginning(5)
    node1.insert_at_beginning(6)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(3)
    node1.display()
    node2 = LinkedList()
    node2.insert_at_beginning(4)
    node2.insert_at_beginning(5)
    node2.insert_at_beginning(6)
    node2.insert_at_beginning(8)
    node2.insert_at_beginning(9)
    node2.insert_at_beginning(4)
    node2.display()
    print(check_intersection(node1, node2))


main()
