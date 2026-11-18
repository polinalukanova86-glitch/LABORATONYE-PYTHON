n = int(input())
numbers = list(map(int, input().split()))
# Список содержит n элементов.
print(numbers[-5:])
print(numbers[1::2])
print(numbers[:1:-1])
