class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def display(self):
        if not self.head:
            return
        current = self.head
        while current.next:
            print(f"{current.data}->", end="")
            current = current.next
        print(current.data)


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(3)
    node1.insert_at_beginning(4)
    node1.insert_at_beginning(5)
    node1.insert_at_beginning(6)
    node1.display()


main()