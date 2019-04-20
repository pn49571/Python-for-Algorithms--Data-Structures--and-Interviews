'''find all pairs of an integer array whose sum is equal to a given number'''
'''1) Initialize an empty hash table s.
2) Do following for each element A[i] in A[]
   (a)    If s[x - A[i]] is set then print the pair (A[i], x - A[i])
   (b)    Insert A[i] into s.'''

def sumpairs(arr,sum):
    hash = []

    for i,j in enumerate(arr):
        if len(hash) == 0:
            hash.append(i)
        if (sum - j) in hash:
            print("Number found: {} and {}".format(j,sum-j))
        else:
            hash.append(j)

if __name__ == '__main__':
    sumpairs([1, 4, 45, 6, 10, -8],16)
