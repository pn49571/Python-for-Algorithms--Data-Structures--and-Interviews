array = [34, -50, 42, 14, -5, 86]

current_max = 0
for i in range(len(array)-1):
    for j in range(i, len(array)+1):
        current_max = max(current_max,sum(array[i:j]))

print(current_max)

max_ending_here = max_so_far = 0
for x in array:
    max_ending_here = max(x, max_ending_here + x)
    max_so_far = max(max_so_far, max_ending_here)
print(max_so_far)

#follow-up wrap

min_ending_here = min_so_far = 0
for x in array:
    min_ending_here = min(x, min_ending_here + x)
    min_so_far = min(min_so_far, min_ending_here)
print(min_so_far)

max_subarray_sum_wraparound = sum(array) - min_so_far

print(max(max_subarray_sum_wraparound, max_so_far))
