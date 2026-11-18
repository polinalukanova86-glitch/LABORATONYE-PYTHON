m = int(input())
n = int(input())
total = 0
for i in range(1, m + 1):
    total += i ** 2
    if total > n:
        break
print(total)
