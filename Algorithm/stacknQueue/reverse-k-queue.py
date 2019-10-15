from Algorithm.stacknQueue.Queue import myQueue
from Algorithm.stacknQueue.stack import myStack

def reverseQueue(queue,k):
    if queue.isEmpty():
        return None
    stack = myStack()

    for index in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty():
        queue.enqueue(stack.pop())

    for i in range(len(queue.queueList) - k):
        queue.enqueue(queue.dequeue())

    return queue



if __name__ == '__main__':
    queue = myQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("Before queue")
    print(queue.queueList)
    reverseQueue(queue, 5)
    print("After queue")
    print(queue.queueList)

