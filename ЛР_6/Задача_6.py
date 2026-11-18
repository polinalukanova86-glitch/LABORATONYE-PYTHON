# Файл text.txt должен лежать рядом с программой.
from pathlib import Path
folder = Path(__file__).resolve().parent
with (folder / 'text.txt').open(encoding='utf-8') as file:
    for line in file:
        print(line.rstrip('\r\n')[::-1])
