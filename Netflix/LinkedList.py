class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def create_linked_list(self, list):
        for val in list:
            self.append(val)
        return

    def print_list(self):
        list_holder = []
        current_node = self.head
        while current_node:
            list_holder.append(current_node.data)
            current_node = current_node.next
        print(list_holder)