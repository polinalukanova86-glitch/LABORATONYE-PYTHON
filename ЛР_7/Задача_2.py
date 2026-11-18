number = input().strip()
digits = set(number.lstrip('-'))
print('Цифры:', ' '.join(sorted(digits)))
print('Количество:', len(digits))
