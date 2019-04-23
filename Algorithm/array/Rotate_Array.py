# To rotate by one, store arr[0] in a temporary variable temp, move arr[1] to arr[0], arr[2] to arr[1] …
# and finally temp to arr[n-1]
#
# Let us take the same example arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
# Rotate arr[] by one 2 times
# We get [2, 3, 4, 5, 6, 7, 1] after first rotation and [ 3, 4, 5, 6, 7, 1, 2] after second rotation.

class RotateArray:
    def __init__(self, array, length, distance, rotation):
        self.array = array
        self.length = length
        self.distance = distance
        if rotation == "left":
            self.__leftRotate()
        elif rotation == "right":
            self.__rightRotate()
        else:
            print("Provide a valid rotation direction: either left or right")

    def __leftRotate(self):
        for i in range(self.distance):
            self.__left_rotateby_one()

    def __left_rotateby_one(self):
        temp = self.array[0]
        for i in range(self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = temp

    def __rightRotate(self):
        for i in range(self.distance):
            self.__right_rotateby_one()

    def __right_rotateby_one(self):
        temp = self.array[self.length-1]
        for i in range(self.length - 1, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = temp

    def get_sorted(self):
        return self.array

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    # arr = [7,1,2,3,4,5,6]
    x = RotateArray(arr, len(arr), 5,"right")
    print(x.get_sorted())
