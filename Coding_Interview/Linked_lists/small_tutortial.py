# We'll start by creating a Node class,
# which represents a single node in the
# linked list. Each node contains two main
# components: the data it holds and a
# reference to the next node.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Next, we'll create the LinkedList class,
# which will handle the operations related
# to the linked list, such as insertion,
# deletion, searching, etc.


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        # To print the contents of the linked list,
        # we need to traverse through each node and
        # print its data.
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert_at_beginning(self, data):
        # Method to insert a new node at the
        # beginning of the linked list.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # insert a node at the end of the
        # linked list, we need to traverse
        # to the last node and then add the new node.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        # To delete a node from the linked list,
        # we need to find the node and update
        # the references to bypass it.
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        # search for a value in the linked list, we
        # can traverse the list and compare each
        # node's data with the target value.
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


def main():
    # Create an instance of the LinkedList class
    my_list = LinkedList()
    # Insert nodes
    my_list.insert_at_beginning(3)
    my_list.insert_at_beginning(2)
    my_list.insert_at_beginning(1)
    my_list.insert_at_end(4)
    # Display the linked list
    my_list.display()  # Output: 1 2 3 4
    # Delete a node
    my_list.delete(2)
    # Display the linked list after deletion
    my_list.display()  # Output: 1 3 4
    # Search for a value
    print(my_list.search(3))  # Output: True
    print(my_list.search(5))  # Output: False


main()
