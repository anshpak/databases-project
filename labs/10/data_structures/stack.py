class Node:
    def __init__(self, value, action, entity):
        self.value = value
        self.action = action
        self.entity = entity
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head', 'system', None)
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            print('No changes were made.')
        return self.head.next.value

    def push(self, value, action, entity):
        node = Node(value, action, entity)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('No changes were made.')
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove

