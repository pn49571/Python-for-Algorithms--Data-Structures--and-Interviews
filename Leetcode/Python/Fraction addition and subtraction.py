import re,math
def fractionAddition(expression):
    ints = map(int, re.findall('[+-]?\d+', expression))
    print(list(ints))
    A, B = 0, 1
    for a in ints:
        b = next(ints)
        A = A * b + a * B
        B *= b
        g = math.gcd(A, B)
        print(g)
        A //= g
        B //= g
    return '%d/%d' % (A, B)
