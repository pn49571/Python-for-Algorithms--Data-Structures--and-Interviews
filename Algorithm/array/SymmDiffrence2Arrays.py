'''
An Efficient solution for find the symmetric difference of two sorted arrays is similar to merge process of merge sort.
We traverse both arrays simultaneously and print smaller element if current two elements do not match and move ahead in
 array with smaller element. Else we ignore the elements and move ahead in both arrays.
'''

def symDiff(buffer):
    "Define the pointers for each array"
    i = 0
    j = 0
    results = []
    arr1 = buffer[0]
    arr2 = buffer[1]

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if arr1[i] not in results:
                results.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if arr1[j] not in results:
                results.append(arr1[j])
            j += 1
        else:
            i += 1
            j += 1

    while i < len(arr1):
        if arr1[i] not in results:
            results.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] not in results:
            results.append(arr2[j])
        j += 1

    return results


if __name__ == '__main__':
    print(symDiff([[1, 2, 3], [5, 2, 1, 4]]))

