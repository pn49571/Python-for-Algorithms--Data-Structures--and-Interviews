'''Recursive python program to reverse an array '''

def reverse(arr,start,end):
    if start >= end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    reverse(arr,start+1,end-1)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print(reverse(arr,0,2))
    print(arr)
