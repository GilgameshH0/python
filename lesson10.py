# Оператор IF

print(2 > 3)
print(3 == 3)

x = 0
if x:
    print('x вернула истину')
else:
    print('x вернула ложь')

light = 'red'
if light == 'red':
    print('stop')
elif light == 'yellow':
    print('wait')
elif light == 'green':
    print('Go!')
else:
    print('What')

age = int(input('Сколько вам лет? '))
if age >= 18:
    print('ура хах')
else:
    print('Вам еще рано!')

time = 12
if time < 12 or time > 13:
    print('открыто')
else:
    print('close')

# Операторы or and != == not

x = 0
if not x:
    print('OK')
else:
    print('No')

# Также может быть такое

res = 'OK' if x else 'NO' # задаем значение переменной res - OK, затем, если x возвращает истину,
print(res) # Тогда ничо не делаем, иначе возвращаем No
