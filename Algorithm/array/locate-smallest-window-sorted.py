array = [3,7,5,6,9]

left, right = None, None
s = sorted(array)

for i in range(len(array)):
    if array[i] != s[i] and left is None:
        left = i
    elif array[i] != s[i]:
        right = i

print(left, right)

left, right = None,None
n = len(array)
max_seen, min_seen = -float("inf"), float("inf")

for i in range(n):
    max_seen = max(max_seen, array[i])
    if array[i] < max_seen:
        right = i

for i in range(n-1,-1,-1):
    min_seen = min(min_seen, array[i])
    if array[i] > min_seen:
        left = i

print(left, right)