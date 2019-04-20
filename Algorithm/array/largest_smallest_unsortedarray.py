'''find the largest and smallest number in an unsorted integer array'''

def largestsmallest(arr):
    largest = arr[0]
    smallest = arr[0]

    for item in arr:
       if item > largest:
           largest = item
       elif item < smallest:
           smallest = item

    return largest,smallest

if __name__ == '__main__':
    print((largestsmallest([32,43,53,54,32,65,63,98,43,23])))