import math

ans = 0
i=0
j=0

string = "pwwkew"
n = len(string)
hashT = []

while(i< n and j<n):
    if string[j] not in hashT:
        hashT.append(string[j])
        j += 1
        ans = max(ans,j-i)
    else:
        hashT.remove(string[i])
        i += 1
print(ans)


###Pseudocode - brute force
#1. iterate the string with j and put that in the hash table. In this process, note down the maximum
#2. If a duplicate character is found at the hash table, remove the characters in the dictionary
#   from 0 to duplicate character. in this process increment the I value
#3. Follow the step 1 and 2 until either I or J is length of array size.