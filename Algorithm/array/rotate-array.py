class RotateArray:
    def __init__(self, array, rotation):
        self.array = array
        self.rotation = rotation

    def run(self):
        return self.array[-self.rotation:] + self.array[:-self.rotation]


def rotation(array):
    temp = []
    for index in range(len(array)-1,-1,-1):
        temp.append(array[index])
    return temp


if __name__ == '__main__':
    arr = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]
    arr = RotateArray(arr, 2).run()
    for i in range(0, len(arr)):
        print(str(arr[i]) + ", ")

    print(rotation([1,2,3,4,5,6]))