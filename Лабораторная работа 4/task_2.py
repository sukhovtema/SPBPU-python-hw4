import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, 'r') as input_file:
            csv_reader = csv.DictReader(input_file)
            data = [row for row in csv_reader]

        json_data = json.dumps(data, indent=4)

        with open(OUTPUT_FILENAME, 'w') as output_file:
            output_file.write(json_data)

    except Exception as e:
        print(f'Ошибка: {e}')


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
