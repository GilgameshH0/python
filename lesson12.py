# Списки

l = [1,2,3, 'hello', ['test', 20], 'world', True] # первый способ

l2 = list('Hello') # Второй способ
l3 = list((1,2,3)) # Третий
l4 = [i for i  in 'hello'] # Четвертый способ

# Вырезать пробел и e из списка!
l5 = [i for i  in 'hello world' if i != ' ' and i !='e'] 
# или можно задать так:
l6 = [i for i  in 'hello world' if i not in ['a','e','i', 'o', ' ']] 
# Можно увеличить буквы
l7 = [i * 3 for i  in 'hello world' if i not in ['a','e','i', 'o', ' ']] 
print(l, l2, l3, l7, sep='\n')


# range()
l8 = list(range(1,11)) # список от 1 до 10 включительно
l8 = list(range(0,11,2 )) # список от 0 до 10 включительно с шагом 2  

for i in range(1,3): # выводит От еденицы включительно до 2
    print(f'Внешний цикл #{i}')
    for j in range(1,3):
        print(f'\tВнутренний цикл #{j}') # выводит От еденицы включительно до 2 \t - табуляция
