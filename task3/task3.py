import json
import sys


def load_json(file_path):
    """Загрузка данных из JSON-файла."""
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_values(tests, values_map):
    """Заполнение полей 'value' в тестах на основе данных из values_map."""
    for test in tests:
        test_id = test.get('id')
        if test_id in values_map:
            test['value'] = values_map[test_id]

        if 'values' in test:
            fill_values(test['values'], values_map)


def save_json(file_path, data):
    """Сохранение данных в формате JSON в указанный файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=1)


def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    values_map = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_map)

    save_json(report_path, tests_data)
    print(f'Отчет сохранен в {report_path}')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Ошибка: Ожидается три аргумента - пути к файлам.')
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)
