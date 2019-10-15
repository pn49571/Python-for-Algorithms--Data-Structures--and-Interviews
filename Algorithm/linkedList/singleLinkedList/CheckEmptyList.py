class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def isEmpty(self):
        if (self.head.next == None):
            return True
        else:
            return False

list = LinkedList()
print(list.isEmpty())