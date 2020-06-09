# Циклы

# While
x = 0
while x < 11:
    x += 1
    print(x, end=' ')

# В функции принт можно добавить разделитель
# и изменить конец строки чтобы не переходило на новую строку
print('hello', 'kek', sep='?', end=' ')


print('heh')

# for
s = "Hello world"
for l in s: # Для каждой буквы в строке
    print(l, end=" ")

for l in s: 
    if l == ' ':
        continue # Чтобы пропустить итерацию
    print(f'"{l}"', end=" ")


for i in 'Hello world':
    if i == ' ':
        break # Выходит из цикла
    print(i, end=' ')
else:
    print('\nNo spaces')
