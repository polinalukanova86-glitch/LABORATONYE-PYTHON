def sum_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

start = int(input())
end = int(input())
print(sum_range(start, end))
