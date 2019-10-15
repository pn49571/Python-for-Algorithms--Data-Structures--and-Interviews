class myQueue:
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return self.size() == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front


if __name__ == '__main__':
    queue = myQueue()

    print("queue.enqueue(2);",queue.enqueue(2))
    print("queue.enqueue(4);",queue.enqueue(4))
    print("queue.enqueue(6);",queue.enqueue(6))
    print("queue.enqueue(8);",queue.enqueue(8))
    print("queue.enqueue(10);",queue.enqueue(10))

    print("Dequeue(): " + str(queue.dequeue()))
    print("Dequeue(): " + str(queue.dequeue()))

    print("front(): " + str(queue.front()))
    print("back(): " + str(queue.back()))

    queue.enqueue(12);
    queue.enqueue(14);

    while queue.isEmpty() == False:
        print("Dequeue(): " + str(queue.dequeue()))

    print("isEmpty(): " + str(queue.isEmpty()))