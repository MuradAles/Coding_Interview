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


def reverse_number(number):
    rev_num = 0
    while number != 0:
        digit = number % 10
        rev_num = rev_num * 10 + digit
        number //= 10
    return rev_num


def sumLists(first_node, second_node):
    # check if one of the node is empty
    if not first_node and not second_node:
        return
    num1, num2 = 0, 0
    while first_node.head:
        num1 = num1*10 + first_node.head.data
        first_node.head = first_node.head.next
    while second_node.head:
        num2 = num2*10 + second_node.head.data
        second_node.head = second_node.head.next
    num1, num2 = reverse_number(num1), reverse_number(num2)
    num3 = num1 + num2
    new_node = LinkedList()
    while num3 != 0:
        temp = num3 % 10
        new_node.insert_at_beginning(temp)
        num3 //= 10
    return new_node


def main():
    node1 = LinkedList()
    node1.insert_at_beginning(1)
    node1.insert_at_beginning(2)
    node1.insert_at_beginning(3)
    node1.display()
    node2 = LinkedList()
    node2.insert_at_beginning(4)
    node2.insert_at_beginning(5)
    node2.display()
    node3 = sumLists(node1, node2)
    node3.display()


main()
