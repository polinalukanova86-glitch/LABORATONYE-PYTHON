d = {'Магазины': [1227, 550, 420],
     'Автосервис': [800, 250]}
total = 0
for expenses in d.values():
    total += sum(expenses)
print(total)
