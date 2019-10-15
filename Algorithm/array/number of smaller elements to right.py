import bisect

array = [3,4,9,6,1]
result = []
for i, num in enumerate(array):
    count = sum([num > val for val in array[i+1:]])
    result.append(count)

print(result)

result = []
seen = []

for num in reversed(array):
    i = bisect.bisect_left(seen, num)
    result.append(i)
    bisect.insort(seen, num)

print(list(reversed(result)))