def custom_write(file_name, strings):
  """
  Записывает строки в файл и возвращает словарь с позициями строк.

  Args:
    file_name: Название файла для записи.
    strings: Список строк для записи.

  Returns:
    Словарь, где ключ - кортеж (номер строки, байт начала строки), а значение - строка.
  """
  strings_positions = {}
  with open(file_name, 'w', encoding='utf-8') as file:
    for i, string in enumerate(strings, 1):
      strings_positions[(i, file.tell())] = string
      file.write(string + '\n')
  return strings_positions
#Записывать в файл file_name все строки из списка strings, каждая на новой строке.
#Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
#а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)