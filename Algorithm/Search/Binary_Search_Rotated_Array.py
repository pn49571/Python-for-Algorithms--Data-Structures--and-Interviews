from Algorithm.array import Shift_Array

class Binary_Search_Rotated:
    def __init__(self, array, key):
        self.array = array
        self.key = key
        self.result = self.run()

    def run(self):
        st = 0
        end = len(self.array) -1
        if st > end :
            return -1
        while st <= end:
            mid = st + (end - st)//2

            if self.array[mid] == self.key:
                return mid

            if self.array[st] <= self.array[mid] and self.array[mid] >= self.key >= self.array[st]:
                end = mid-1
            elif self.array[end] >= self.array[mid] and self.array[mid] <= self.key <= self.array[end]:
                st = mid + 1
            elif self.array[st] >= self.array[mid]:
                end = mid - 1
            elif self.array[end] <= self.array[mid]:
                st = mid + 1

        return -1

    def __repr__(self):
        return str(self.result)


v1 = [1, 2, 3, 4, 5, 6, 7]
x = Shift_Array.ShiftArray(v1, len(v1), 2).get_sorted()
print("Key(3) found at: " + str(Binary_Search_Rotated(x, 3)))
print("Key(6) found at: " + str(Binary_Search_Rotated(x, 6)))

v2 = [1, 2, 3, 4, 5, 6]
x = Shift_Array.ShiftArray(v1, len(v1), 2).get_sorted()
print("Key(3) found at: " + str(Binary_Search_Rotated(x, 3)))
print("Key(6) found at: " + str(Binary_Search_Rotated(x, 6)))