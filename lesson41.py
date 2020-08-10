# Регулярные выражения re

import re


s = 'Это просто строка, строкач'
a = 'Первое. Второе. Третье.'
pattern = 'строка'

if re.search(pattern, s):
    print('sucess')
else:
    print('no match')

match = re.search(pattern,s)
print(match)
print(match.start(), match.end()) # начало и конец входа
print(re.findall(pattern,s)) # массив строк с такими строками
print(re.split('\.', a)) # слеш экранирует символ и рассматривает как специальный символ
print(re.split(r'\.', a, 1)) # либо импользовать r. 1 - количество разделений только один раз
