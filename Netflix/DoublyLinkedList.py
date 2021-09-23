class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        current_node = Node(data)
        if self.head == None:
            self.head = current_node
            self.tail = current_node
        else:
            current_node.next = self.head
            self.head.prev = current_node
            self.head = current_node

        self.size += 1

    def insert_at_tail(self, data):
        current_node = Node(data)
        if self.tail == None:
            self.tail = current_node
            self.head = current_node
            current_node.next = None
        else:
            self.tail.next = current_node
            current_node.prev = self.tail
            self.tail = current_node
            current_node.next = None

        self.size += 1