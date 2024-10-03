import sys


def read_numbers_from_file(file_path):
    """Чтение чисел из файла и возврат в виде списка."""
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f'Ошибка: {line.strip()} не является целым числом.')
                sys.exit(1)
    return numbers


def calculate_min_moves(nums):
    """
    Вычисление минимального количества ходов
    для приведения всех чисел к медиане.
    """
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


def main(file_path):
    nums = read_numbers_from_file(file_path)
    min_moves = calculate_min_moves(nums)
    print(min_moves)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Ошибка: Ожидается один аргумент - путь к файлу.')
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
