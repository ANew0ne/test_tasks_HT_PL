import sys


if len(sys.argv) != 3:
    print('Ошибка: Ожидается два аргумента командной строки: n и m.')
    sys.exit(1)

try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except ValueError:
    print('Ошибка: Аргументы должны быть целыми числами.')
    sys.exit(1)

if n <= 0 or m <= 1:
    print('Значения n должно быть больше 0, а m больше 1.')
    sys.exit(1)

array = list(range(1, n + 1))
path = []
index = 0

for i in range(n):
    path.append(array[index])
    index = (index + m - 1) % n

    if index == 0:
        break

print('Полученный путь:', ''.join(map(str, path)))
