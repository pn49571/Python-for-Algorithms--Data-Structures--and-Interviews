def getmedian(arr1,arr2,n):
    if n == 0:
        return -1
    elif n == 1:
        return (arr1[0] + arr2[0])/2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + max(arr1[1],arr2[1]))/2
    else:
        #1. Calculate the medians m1 and m2 of the input arrays ar1[]  and ar2[] respectively
        marr1 = median(arr1,len(arr1))
        marr2 = median(arr2,len(arr2))
        #2) If m1 and m2 both are equal then we are done. return m1 (or m2)
        # 3) If m1 is greater than m2, then median is present in one of the below two sub arrays.
        # a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
        # b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
        # 4) If
        # m2 is greater
        # than
        # m1, then
        # median is present in one
        # of
        # the
        # below
        # two
        # subarrays.
        #     a)  From
        # m1
        # to
        # last
        # element
        # of
        # ar1(ar1[ | _n / 2
        # _ | ...
        # n - 1])
        # b)  From
        # first
        # element
        # of
        # ar2
        # to
        # m2(ar2[0... | _n / 2
        # _ |])
        # 5) Repeat
        # the
        # above
        # process
        # until
        # size
        # of
        # both
        # the
        # subarrays
        # becomes
        # 2.
        # 6) If
        # size
        # of
        # the
        # two
        # arrays is 2
        # then
        # use
        # below
        # formula
        # to
        # get
        # the
        # median.
        Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1])) / 2
        Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1])) / 2
        if marr1 > marr2:
            if n % 2 == 0:
                return getmedian(arr1[:int(n/2) + 1], arr2[int(n/2) -1:], int(n/2) + 1)
            else:
                return getmedian(arr1[:int(n/2) + 1], arr2[int(n/2):], int(n/2) + 1)
        else:
            if n % 2 == 0:
                return getmedian(arr1[int(n/2)-1:],arr2[:int(n/2) + 1], int(n/2) + 1)
            else:
                return getmedian(arr1[int(n/2):],arr2[:int(n/2) + 1], int(n/2) + 1)

if marr1 == marr2:
    print("The median is found {}".format(marr1))

print(marr1,marr2)


# if marr1 > marr2:
#     if marr1 in arr1:
#         arrm1 = arr1.index(marr1)
#     else:
#         for x in arr1:

arr1 = [1,12,15,26,38]
arr2 = [2,13,17,30,45]


def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]
