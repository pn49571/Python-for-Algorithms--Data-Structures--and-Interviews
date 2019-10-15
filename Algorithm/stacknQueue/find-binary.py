from Algorithm.stacknQueue.Queue import myQueue

def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    for item in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[item] + '0'
        s2 = result[item] + '1'
        queue.enqueue(s1)
        queue.enqueue(s2)
    return result


if __name__ == '__main__':
    findBin(3)
