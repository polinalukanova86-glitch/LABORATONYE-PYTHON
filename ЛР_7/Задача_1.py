players = []
for _ in range(5):
    surname, height = input().split()
    players.append((int(height), surname))
players.sort()
for height, surname in players:
    print(height, '-', surname)
