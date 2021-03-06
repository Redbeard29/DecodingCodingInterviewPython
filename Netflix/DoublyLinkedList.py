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
            self.head.prev = current_node
            current_node.next = self.head
            self.head = current_node

        self.size += 1
        return current_node

    def remove_tail(self):
        if self.size == 0:
            return None

        removed = self.tail
        
        removed.prev.next = None
        self.tail = removed.prev
        removed.prev = None

        self.size -= 1
        return removed

    def move_front(self, node):
        if node is None:
            return None
        
        elif node is self.head:
            return node

        elif node is self.tail:
            node.prev.next = None
            self.tail = node.prev

        else:
            #Remove node from current location
            node.next.prev = node.prev
            node.prev.next = node.next

        #Update node to become head
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

        return node


    def print_list(self):
        list_holder = []
        current_node = self.head
        
        while current_node:
            list_holder.append({'current': (current_node.data.key, current_node.data.val), 
            'next': (current_node.next.data.key, current_node.next.data.val) if current_node.next else None, 
            'prev': (current_node.prev.data.key, current_node.prev.data.val) if current_node.prev else None})
            current_node = current_node.next
        print(list_holder)

    def get_size(self):
        print(self.size)


