import json


def task() -> float:
    try:
        with open('input.json', 'r') as file:
            data = json.load(file)
            total_sum = 0

            for item in data:
                total_sum += item['score'] * item['weight']

            total_sum = round(total_sum, 3)
            return total_sum
    except Exception as e:
        print(f'Ошибка: {e}')
        return 0.0


print(task())
