class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        if not all:
            while node is not None:
                del_node = node
                if node.value == val and node == self.tail and node == self.head:
                    self.head = None
                    self.tail = None
                    node = None
                    del_node = None
                    break
                elif node.value == val and node == self.head:
                    self.head = node.next
                    del_node.next = None
                    del_node = None
                    node = self.head
                    if node is not None:
                        node.prev = None
                    break
                elif node.value == val and node != self.tail:
                    prev_node.next = node.next
                    next_node = node.next
                    next_node.prev = prev_node
                    node = node.next
                    del_node.prev = None
                    del_node.next = None
                    del_node = None
                    break
                elif node.value == val and node == self.tail:
                    prev_node.next = None
                    node.prev = None
                    node.next = None
                    node = None
                    self.tail = prev_node
                    del_node = None
                    break
                prev_node = node
                node = node.next
        else:
            while node is not None:
                del_node = node
                if node.value == val and node == self.head and node != self.tail:
                    self.head = node.next
                    node = node.next
                    node.prev = None
                    del_node.next = None
                    del_node = None
                    
                elif node.value == val and node != self.tail:
                    prev_node.next = node.next
                    next_node = node.next
                    next_node.prev = prev_node
                    node = node.next
                    del_node.prev = None
                    del_node.next = None
                    del_node = None
                elif node.value == val and node == self.tail and node == self.head:
                    node.prev = None
                    node.next = None
                    node = None
                    del_node = None
                    next_node = None
                    self.head = None
                    self.tail = None
                    break
                    
                elif node.value == val and node == self.tail:
                    prev_node.next = None
                    node.prev = None
                    node.next = None
                    node = None
                    self.tail = prev_node
                    del_node = None
                    next_node = None
                    break
                if node.value != val:
                    prev_node = node
                if node.value != val:
                    node = node.next

    def clean(self):
        node = self.head
        self.head = None
        self.tail = None
        while node is not None:
            del_node = node
            node = node.next
            del_node.prev = None
            del_node.next = None
            del_node = None


    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
            node = self.head
        else:
            node = self.head
        while node is not None:
            if node.next is not None:
                next_node = node.next
            if node == afterNode and node != self.tail:
                afterNode.next = newNode
                newNode.prev = afterNode
                newNode.next = next_node
                next_node.prev = newNode
                break
            elif afterNode is None and self.head is None and self.tail is None:
                if self.head is None:
                    self.head = newNode
                    newNode.prev = None
                    newNode.next = None
                else:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                self.tail = item
                break
            elif self.head == newNode and self.tail == newNode and node == newNode:
                break
            elif afterNode is None and self.head is not None and self.tail is not None:
                node = self.tail
                node.next = newNode
                self.tail = newNode
                newNode.prev = node
                break
            elif node == afterNode and node == self.tail:
                afterNode.next = newNode
                newNode.prev = afterNode
                self.tail = newNode
                break
            node = node.next
    def add_in_head(self, newNode):
        node = self.head
        if node is not None and node != self.tail:
            self.head = newNode
            node.prev = newNode
            newNode.next = node
        elif node is not None and node == self.tail and node == self.head:
            self.head = newNode
            node.prev = newNode
            newNode.next = node
        elif node is None:
            self.head = newNode
            self.tail = newNode