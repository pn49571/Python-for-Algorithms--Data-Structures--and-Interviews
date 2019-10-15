class SmallestCommon:
    def __init__(self, array1, array2, array3):
        self.array1 = array1
        self.array2 = array2
        self.array3 = array3

    def run(self):
        i, j, k = 0,0,0

        while i < len(self.array1) and j < len(self.array2) and k < len(self.array3):

            # Finding the smallest common number
            if self.array1[i] == self.array2[j] and self.array2[j] == self.array3[k]:
                return self.array1[i]

            # Let's increment the iterator for the smallest value

            if self.array1[i] <= self.array2[j] and self.array1[i] <= self.array3[k]:
                i += 1
            elif self.array2[j] <= self.array1[i] and self.array2[j] <= self.array3[k]:
                j += 1
            elif self.array3[k] <= self.array1[i] and self.array3[k] <= self.array2[j]:
                k += 1

        return -1

if __name__ == '__main__':
    v1 = [1, 6, 10, 14, 50]
    v2 = [-1, 6, 7, 8, 50]
    v3 = [0, 6, 7, 10, 25, 30, 50]
    result = SmallestCommon(v1, v2, v3).run()
    print("Least common number: " + str(result))