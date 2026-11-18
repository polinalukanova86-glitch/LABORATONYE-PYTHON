m = abs(int(input()))
n = abs(int(input()))
if m == 0:
    print(n)
elif n == 0:
    print(m)
else:
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    print(m)
