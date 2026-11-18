import random
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = random.choice([-1, 1]) * random.randint(1, 10)
print(numbers)
