class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        current = self.head
        while current.next:
            print(current.data, end="->")
            current = current.next
        print(current.data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_duplicates(self):
        if not self.head:
            return
        current = self.head
        uniq_array = []
        while current.next:
            if current.next.data in uniq_array:
                current.next = current.next.next
            else:
                uniq_array.append(current.next.data)
                current = current.next


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(3)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(5)
    node1.insert_at_beginning(6)
    node1.remove_duplicates()
    node1.display_list()


main()
