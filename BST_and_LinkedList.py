class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add_value(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def remove_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    def display(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        print("->".join(nodes) if nodes else "List is empty")
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if current.value > value:
                if current.left is  None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is  None:
                    current.right = new_node
                    break
                current = current.right



ll = LinkedList()
ll.add_value(5)
ll.add_value(6)
ll.add_value(7)
ll.remove_value(6)
#print(ll.head.next.data)
#ll.display()

bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(6)
print(bst.root.left.value)
