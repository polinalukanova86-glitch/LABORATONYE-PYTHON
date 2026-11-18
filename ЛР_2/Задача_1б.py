a = int(input())
b = int(input())
if a >= b:
    maximum, minimum = a, b
else:
    maximum, minimum = b, a
print('Максимум:', maximum)
print('Минимум:', minimum)
