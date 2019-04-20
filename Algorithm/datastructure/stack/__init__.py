class stack:
    def __init__(self):
        self.top = 0
        self.data = []

    def empty(self):
        return (self.top == 0)

    def push(self,item):
        if self.top < len(self.data):
            self.data[self.top] = item
        else:
            self.data.append(item)

        self.top += 1

    def pop(self):
        if self.empty():
            return None
        else:
            self.top -= 1
            return self.data[self.top]

    def display(self):
        return [self.data[x] for x in range(self.top)]


if __name__ == '__main__':
    x = stack()
    x.push(5)
    x.push(6)
    x.push(1)
    print(x.display())
    x.pop()
    x.pop()
    print(x.display())
    print(x.empty())
    x.push(200)
    print(x.display())
