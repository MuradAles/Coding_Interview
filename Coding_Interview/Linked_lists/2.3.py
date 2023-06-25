class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            return
        current = self.head
        while current.next:
            print(f"{current.data}->", end="")
            current = current.next
        print(current.data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_in_middle(self):
        if not self.head:
            return
        length = 0
        current = self.head
        while current:
            current = current.next
            length += 1
        current = self.head
        # mid = length//2 - (length % 2 == 0)
        mid = (length // 2 - 1) if (length) % 2 == 0 else (length // 2)
        for i in range(0, mid):
            current = current.next
        current.data = current.next.data
        current.next = current.next.next
        return current.data


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(6)
    node1.insert_at_beginning(5)
    node1.insert_at_beginning(4)
    node1.insert_at_beginning(3)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(1)
    node1.delete_in_middle()
    node1.display()


main()
