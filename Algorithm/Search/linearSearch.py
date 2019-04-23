class LinearSearch:
    def __init__(self, array, key):
        self.array = array
        self.key  = key

    def run(self):
        for index,item in enumerate(self.array):
            if item == self.key:
                return index
        return -1

if __name__ == '__main__':
    arr = [5, 3, 2, 9, 7]
    arr.sort()
    x  = LinearSearch(arr, 7)
    print(x.run())



