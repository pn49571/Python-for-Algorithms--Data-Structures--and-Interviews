class myStack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return len(self.stackList) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()


if __name__ == '__main__':
    stack = myStack()
    for i in range(5):  # Pushing values in
        stack.push(i)
        print("top(): " + str(stack.top()))

    for x in range(5):  # Removing values
        stack.pop()

    print("isEmpty(): " + str(stack.isEmpty()))  # Checking if its empty
    print("top() " + str(stack.top()))
    print("size() " + str(stack.size()))

