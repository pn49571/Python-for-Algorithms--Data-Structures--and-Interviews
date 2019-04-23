class BinarySearch:
    def __init__(self, array, key, low, high):
        self.array = array
        self.key  = key
        self.low = low
        self.high = high

    def run(self):
        if self.low > self.high:
            return -1
        mid = self.low + (self.high - self.low) // 2
        if self.array[mid] == self.key:
            return mid
        elif self.key > mid:
            return BinarySearch(self.array, self.key, mid + 1, self.high).run()
        else:
            return BinarySearch(self.array, self.key, self.low, mid - 1).run()



if __name__ == '__main__':
    arr = [5, 3, 2, 9, 7]
    arr.sort()
    x = BinarySearch(arr, 10, 0, len(arr) - 1)
    print(x.run())
