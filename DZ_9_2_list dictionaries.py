first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список с длиной строк из first_strings, где длина строк не менее 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

# 2. Список кортежей слов одинаковой длины из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь с парами ключ-значение: строка-длина строки из объединённых списков, где чётная длина строки
combined_strings = first_strings + second_strings
third_result = {string: len(string) for string in combined_strings if len(string) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)


### Результаты:
#- first_result: длины строк из first_strings, которые содержат не менее 5 символов.
#- second_result: список кортежей из слов одинаковой длины.
#- third_result: словарь, где ключ – строка, а значение – её длина, только для строк с чётной длиной.

#Вывод значений будет таким: