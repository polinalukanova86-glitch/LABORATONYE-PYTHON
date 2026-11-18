a = float(input())
b = float(input())
if a <= 0 and b > a:
    print('Невозможно определить день')
else:
    day = 1
    while a + 1e-10 < b:
        a *= 1.15
        day += 1
    print(day)
