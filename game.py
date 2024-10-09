from string import ascii_letters
print("Hello")
print(ord('h')) #оператор вызоваа кодировки
a = 'hello'
chars = []

for i in a:
    chars.append(ord(i))
s = ''
print(chars)
for i in chars:
    s +=chr(i)# оператор обратно преобразующий кодтровку в символы
print(s)

print(hex(ord('h'))) #переводим символ в численное прелставление, затем в hex 16ричный формат
bb = b'\x68' #байтовое представление строки
print(bb.decode()) #перевод из hex представления вобычное
