ans = 0
string = "abcabcbb"
n = len(string)

def allunique(strin):
    hashT = []
    for i in  strin:
        if i not in hashT:
            hashT.append(i)
        else:
            return False
    return True

for i in range(0, n-1):
    for j in range(i+1, n):
        if allunique(string[i:j]):
            maxi = max(ans,j-i)
            if maxi > ans:
                print(string[i:j])
                ans = maxi

print(ans)

###Pseudocode - brute force
#1. iterate the string with 2 pointers with 2 for loops.
#   i = 0 to n-1
#   j = i+1 to n
#2. for each iteration, check if the string has all unique characters and record if the unique is true