from collections import deque

def find_max_sliding_window(arr, window_size):
    if len(arr) == 0:
        return

    if window_size > len(arr):
        return

    window = deque()

    result = []
    print(window)

    # find out max for first window
    for i in range(0, window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)

    result.append(arr[window[0]])

    for i in range(window_size, len(arr)):
        # remove all numbers that are smaller than current number
        # from the tail of list
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window anymore
        if window and (window[0] <= i - window_size):
            window.popleft()

        window.append(i)
        result.append(arr[window[0]])

    return result


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array = " + str(array))

print("Max = " + str(find_max_sliding_window(array, 3)))

array = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
print("Array = " + str(array))

print("Max = " + str(find_max_sliding_window(array, 3)))