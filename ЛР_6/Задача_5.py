# Файл input.txt должен лежать рядом с программой.
from pathlib import Path
folder = Path(__file__).resolve().parent
numbers = list(map(int, (folder / 'input.txt').read_text(encoding='utf-8').split()))
numbers.sort()
(folder / 'output.txt').write_text(' '.join(map(str, numbers)), encoding='utf-8')
print('Числа отсортированы и записаны в output.txt')
