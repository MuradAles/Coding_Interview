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

    def loop_detection(self):
        if not self.head:
            return
        fastptr = self.head
        slowptr = self.head
        while fastptr is not None and fastptr.next is not None:
            # Move slow pointer by 1 node and fast at 2 at each step.
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            # If both the pointers meet at any point, then the cycle is present and return true...
            if slowptr == fastptr:
                return 1
        return 0


def main():
    node1 = LinkedList()
    node1.insert_at_beginning("C")
    node1.insert_at_beginning("E")
    node1.insert_at_beginning("D")
    node1.insert_at_beginning("C")
    node1.insert_at_beginning("B")
    node1.insert_at_beginning("A")
    node1.display()
    print(node1.loop_detection())


main()
