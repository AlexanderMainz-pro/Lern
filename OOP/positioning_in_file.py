from pprint import pprint

""""когда мы работаем с файлом, мы работаем с невидимым курсором
не забываем переключать на нужное действие в open вторым аргументом"""
name = 'sample2.txt'
file = open(name, 'a', encoding='utf-8') # r, w, a, read, write, append
pprint(file.writable()) #возврщает булево значение, можно ли записать в файл что-гибуть
pprint(file.readable()) #возврщает булево значение, можно ли прочитьать что либо из текста
pprint(file.seekable()) #возврщает булево значение, можно ли перемещать курсор в тексте
print(file.tell()) #поекзать позицию курсор
#pprint(file.read()) #считывание файла
#pprint(file.close()) #закрытие файла
file.seek(15)# передвигаем курсор
file.write('new text')
print(file.tell())
file.close()

with open(name, encoding='utf-8') as file:
    for line in file:
       for char in line:
        print(line, end='')
# явно можем выделить, где происходит открытие и зкрытие файла