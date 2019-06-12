class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class Queues:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enque(self, val):
        new_node = node(val)
        if (self.head and self.tail == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

    def deque(self):
        if self.head=None:
            return self
        if self.head.next = None:
            self.head = None
            self.tail = None
            return self

        val = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return val
        
        