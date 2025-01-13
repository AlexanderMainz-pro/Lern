print('Hello' + 'world')
print('Hello' + str(14))
print("my name  %s" % 'Ales')#устаревший способ конкатенации, только один аргумент, модо добавить в виде кортежа
#print('My name %(name)s, I am so old %s(yeas)s' % {'name': "Alex", 'yeas': 14})
print('my name{}{}'.format('urban', '-university'))
print('my name{0}{1}{0}'.format('urban', '-university'))
print('my name{title}{postfix}{title}'.format(title='urban', postfix='-university'))  #новый метод
#Ф-строка