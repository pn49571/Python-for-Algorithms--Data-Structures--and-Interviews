'''
1. Get the sum of numbers
       total = n*(n+1)/2
2  Subtract all the numbers from sum and
   you will get the missing number.
'''

def missingNum(num):
    n = len(num)
    total = (n+1) * (n+2)/2
    for i in num:
        total -= i
    return int(total)

if __name__ == '__main__':
    print(missingNum([1,2,3,5,6,7,8,9,10]))
