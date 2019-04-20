'''duplicate number on a given integer array'''

def duplicateRem(arr):
    look = []
    for i in arr:
        if i not in look:
            look.append(i)
    return look

if __name__ == '__main__':
    print(duplicateRem([1,2,3,3,3]))
