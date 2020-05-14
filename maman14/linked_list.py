from maman14.node import Node


class List(object):

    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def peak(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def pop(self):
        if self.head is None:
            raise Exception("The Linked List is empty !")

        self.size -= 1

        value = self.head.data

        # If the list has only single node
        if self.head == self.tail:
            self.tail = None

        # Incrementing head to next node
        self.head = self.head.next

        return value

    def add_number(self, data):
        new_node = Node(data)
        self.size += 1

        if self.head is None:  # List is empty
            self.head = new_node
            return

        if self.tail is None:  # List had only one Node
            self.head.next = new_node
            self.tail = new_node
            return

        else:  # List has head and tail
            self.tail.next = new_node
            self.tail = new_node

    def add_list(self, number_list):
        for number in number_list:
            self.add_number(number)

    def __repr__(self):
        # For debugging purpose - represent the linked list
        result = []

        current = self.head

        while current is not None:
            # Append takes O(1) since it's add the item to the end of the list (see reference in word file)
            result.append(current.data)
            current = current.next

        return str(result)

    def __str__(self):
        # To add readability - not essential
        result = ""

        current = self.head
        while current is not None:
            result += str(current.data) + ", "
            current = current.next

        return str(result[:-2])  # cropping the last comma and space


