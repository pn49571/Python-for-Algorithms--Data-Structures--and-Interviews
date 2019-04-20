def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n -1)

if __name__ == '__main__':
    print(power(2,3))