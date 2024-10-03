import sys
import math


def read_circle_data(file_path):
    """Чтение данных окружности из файла."""
    try:
        with open(file_path, 'r') as f:
            center_x, center_y = map(float, f.readline().split())
            radius = float(f.readline().strip())
        return center_x, center_y, radius
    except Exception as e:
        print(f'Ошибка при чтении файла с окружностью: {e}')
        sys.exit(1)


def read_dots_data(file_path):
    """Чтение данных точек из файла."""
    dots = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                x, y = map(float, line.split())
                dots.append((x, y))
        return dots
    except Exception as e:
        print(f'Ошибка при чтении файла с точками: {e}')
        sys.exit(1)


def dot_position(center_x, center_y, radius, dot_x, dot_y):
    """Определение положения точки относительно окружности."""
    distance = math.sqrt((dot_x - center_x) ** 2 + (dot_y - center_y) ** 2)

    if math.isclose(distance, radius):
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Ошибка: Ожидается два аргумента - пути к файлам.')
        sys.exit(1)

    circle_file = sys.argv[1]
    dots_file = sys.argv[2]

    center_x, center_y, radius = read_circle_data(circle_file)
    dots = read_dots_data(dots_file)
    num_dots = len(dots)

    if num_dots < 1 or num_dots > 100:
        print('Ошибка: Количество точек должно быть от 1 до 100. '
              f'Найдено: {num_dots}')
        sys.exit(1)

    for dot_x, dot_y in dots:
        position = dot_position(center_x, center_y, radius, dot_x, dot_y)
        print(f'Точка ({dot_x}, {dot_y}) -> {position}')
