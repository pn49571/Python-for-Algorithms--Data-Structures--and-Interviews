class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insertAtTail(self, dt):
        tempNode = Node(dt)
        if self.isempty():
            self.head.next = tempNode
        else:
            temp = self.head.next
            while temp.next != None:
                temp = temp.next

            temp.next = tempNode
        return self.head

    def isempty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def printList(self):
        if self.isempty():
            print("List is empty")
            return False
        #start with the head
        temp = self.head.next
        while temp.next != None:
            print(" --> {}".format(temp.data))
            temp = temp.next
        print("--> {} --> None".format(temp.data))
        return True

list = LinkedList()
list.printList()

for i in range(1,10,1):
    list.insertAtTail(i)
list.printList()