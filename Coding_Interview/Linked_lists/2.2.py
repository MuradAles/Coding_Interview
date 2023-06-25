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

    def length_of_linkedList(self):
        if not self.head:
            return
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    def return_Kth_to_Last(self, k):
        if not self.head:
            return
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1

        if k > count:
            print("K more than length of Linked List")
            return
        current = self.head
        for i in range(0, count - k):
            current = current.next
        print(current.data)
        return current.data


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(4)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(2)
    node1.return_Kth_to_Last(1)
    node1.display()


main()
