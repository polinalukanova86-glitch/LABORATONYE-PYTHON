n = int(input())
penguin = ['   _~_   ', '  (o o)  ', ' / V \\   ', '/( _ )\\  ', '  ^^ ^^  ']
for line in penguin:
    print(' '.join([line] * n))
