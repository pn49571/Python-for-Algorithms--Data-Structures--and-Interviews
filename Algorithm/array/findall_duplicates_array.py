''' duplicate numbers in an array if it contains multiple duplicates '''

def duplicate(arr):
    hash = {}

    for item in arr:
        if item not in hash.keys():
            hash[item] = 1
        else:
            hash[item] += 1
    return [x for x,y in hash.items() if y > 1]

if __name__ == '__main__':
    print(duplicate([1, 2, 3, 1, 3, 6, 6]))