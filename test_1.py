def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # или можно вернуть None для обработки пустого ввода
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(result)  # Вывод: 30.0