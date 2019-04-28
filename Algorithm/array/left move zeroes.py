class LeftMoveZero:
    def __init__(self, array):
        if len(array) == 0:
            raise Exception("No arrays were given")

        self.array = array

    def run(self):
        readIndex = len(self.array) - 1
        writeIndex = len(self.array) - 1

        while readIndex > 0:
            if self.array[readIndex] != 0:
                self.array[writeIndex] = self.array[readIndex]
                writeIndex -= 1
            readIndex -= 1

        while writeIndex >= 0:
            self.array[writeIndex] = 0
            writeIndex -= 1

        return self.array

if __name__ == '__main__':
    v = [1, 10, -1, 11, 5, 0, -7, 0, 25, -35]
    x = LeftMoveZero(v)
    print(x.run())